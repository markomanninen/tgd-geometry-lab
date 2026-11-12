"""The exact models behind the pictures of the energy video (docs/explainerit/lyhyt-02-energia.md).  The Manim
scene that draws them is kept with the video sources outside the repository, and check.py tests them.

1.  Einstein's curved space-time is a Lemaître-Tolman-Bondi dust solution of Einstein's equations,

        ds^2 = dt^2 - R'(r,t)^2 dr^2 - R(r,t)^2 dOmega^2,    R(r,t) = r (t - t_B(r))^(2/3),

    with the bang time t_B(r) = B exp(-r^2 / W^2).  The dust is denser in the middle, where the bang is later.
    The picture shows the slice theta = pi/2 in the comoving coordinates x = r cos(phi), y = r sin(phi) and t,
    in which the dust stands still, so the vertical lines of the lattice are the world lines of the matter.
    The solution has the three rotations as Killing vectors and no others: no translation and no boost.

2.  The space-time surface of TGD is a surface X^2 in the slice (t, x, s) of H = M^4 x CP2, where t and x are
    coordinates of M^4 and s is the length along a geodesic circle of CP2.  The metric of the slice is
    dt^2 - dx^2 - ds^2, the project's convention h = m + (-s).  The surface is an extremal of the volume term
    of the action, which in two dimensions is the string solution

        X(sigma, tau) = (t, x, s) = (tau, (a(sigma - tau) + a(sigma + tau)) / 2),

    where a(p) is a curve in the (x, s) plane with unit speed.  Two pulses run along the surface with the speed
    of light, one each way, and pass through each other at tau = 0.

    The coordinates are conformal: the induced metric is Omega (dtau^2 - dsigma^2), Omega = (1 + a'(p).a'(q)) / 2.
    The Noether current of a translation xi of M^4 is J^alpha = sqrt(g) g^(alpha beta) h(xi, d_beta X), and for
    the time translation it is J^tau = 1, J^sigma = 0.  As a vector of the surface it is the part of xi along the
    surface, xi_par = X_tau / Omega, and its flow lines are the curves sigma = constant.
"""
import numpy as np

# ---- 1. Lemaître-Tolman-Bondi dust, in units where a = 1 far from the middle at the picture time t = 0

T_REF = 4.0            # cosmic time of the picture time t = 0
B, W = 2.0, 2.0         # height and width of the bang time function
LAM = T_REF ** (2 / 3)


def t_bang(r):
    return B * np.exp(-r * r / W ** 2)


def ltb_slopes(x, y, t):
    """Radial and tangential dx/dt of the light cone at the picture point (x, y, t)."""
    r = np.hypot(x, y)
    u = T_REF + t - t_bang(r)                       # time since the bang at this place
    r_dtb = -2 * r * r / W ** 2 * t_bang(r)         # r t_B'(r)
    r_prime = u ** (2 / 3) - (2 / 3) * r_dtb * u ** (-1 / 3)
    return LAM / r_prime, LAM * u ** (-2 / 3)


# ---- 2. the surface X^2 in the slice (x, s, t) of H

PHI, WP = 1.0, .6      # greatest angle of the curve a against the x axis, and the width of its bump
_P = np.linspace(-12, 12, 9601)


def angle(p):
    return -PHI * (p / WP) * np.exp(.5 - p * p / (2 * WP * WP))


def _integral(f):
    """The integral of f from the first grid point, by Simpson's rule on each step of the grid."""
    mid = f(.5 * (_P[1:] + _P[:-1]))
    v = f(_P)
    return np.concatenate([[0], np.cumsum((v[:-1] + 4 * mid + v[1:]) * np.diff(_P) / 6)])


_AX = _integral(lambda p: np.cos(angle(p)))
_AX -= _AX[len(_P) // 2]                            # a_x(0) = 0
_AS = _integral(lambda p: np.sin(angle(p)))         # a_s(-infinity) = 0


def _hermite(p, values, slope):
    """The curve between the grid points as the cubic that has the right values and slopes at both ends."""
    p = np.asarray(p, dtype=float)
    i = np.clip(np.searchsorted(_P, p) - 1, 0, len(_P) - 2)
    d = _P[i + 1] - _P[i]
    u = (p - _P[i]) / d
    h00, h10, h01, h11 = 2 * u ** 3 - 3 * u ** 2 + 1, u ** 3 - 2 * u ** 2 + u, -2 * u ** 3 + 3 * u ** 2, u ** 3 - u ** 2
    return h00 * values[i] + h10 * d * slope(_P[i]) + h01 * values[i + 1] + h11 * d * slope(_P[i + 1])


def a_x(p):
    return _hermite(p, _AX, lambda v: np.cos(angle(v)))


def a_s(p):
    return _hermite(p, _AS, lambda v: np.sin(angle(v)))


def X(sig, tau):
    """The point of the surface, as (x, s, t)."""
    p, q = sig - tau, sig + tau
    return np.array([.5 * (a_x(p) + a_x(q)), .5 * (a_s(p) + a_s(q)), tau + 0 * p])


def X_tau(sig, tau):
    p, q = angle(sig - tau), angle(sig + tau)
    return np.array([.5 * (np.cos(q) - np.cos(p)), .5 * (np.sin(q) - np.sin(p)), 1.0 + 0 * p])


def X_sig(sig, tau):
    p, q = angle(sig - tau), angle(sig + tau)
    return np.array([.5 * (np.cos(q) + np.cos(p)), .5 * (np.sin(q) + np.sin(p)), 0 * p])


def omega(sig, tau):
    return .5 * (1 + np.cos(angle(sig - tau) - angle(sig + tau)))


def h(u, v):
    """The metric of the slice of H, for vectors (x, s, t)."""
    return u[2] * v[2] - u[0] * v[0] - u[1] * v[1]


def xi_par(sig, tau):
    """The part of the time translation xi = (0, 0, 1) along the surface: the direction of the energy current."""
    return X_tau(sig, tau) / omega(sig, tau)


def nulls(sig, tau):
    """The two light-like directions of the induced metric: where the light cone of H cuts the tangent plane."""
    return X_tau(sig, tau) + X_sig(sig, tau), X_tau(sig, tau) - X_sig(sig, tau)
