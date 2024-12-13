from function import unimodal, multimodal
from framework import PSO, PSOVC, BPSO, Swarm

# 次元数
d = 2

# ベンチマーク関数
func = (
    unimodal.Sphere,
    unimodal.Rosenbrock,
    multimodal.TheNthPowerOfTwoMinma,
    multimodal.Ackley,
    multimodal.Rastrigin,
    multimodal.Griewank,
    multimodal.Schwefel,
)

# シミュレーション
for i in range(len(func)):
    f = func[i]()

    pso = PSO(
        Swarm(
            dimentions=d,
            position_min=f.x_min,
            position_max=f.x_max,
            velocity_max=0.5 * (f.x_max - f.x_min),
            velocity_min=-0.5 * (f.x_max - f.x_min),
        ),
        f,
    )

    psovc = PSOVC(
        Swarm(
            dimentions=d,
            position_min=f.x_min,
            position_max=f.x_max,
            velocity_max=0.5 * (f.x_max - f.x_min),
            velocity_min=-0.5 * (f.x_max - f.x_min),
        ),
        f,
    )

    bpso = BPSO(
        Swarm(
            dimentions=d,
            position_min=f.x_min,
            position_max=f.x_max,
            velocity_max=0.5 * (f.x_max - f.x_min),
            velocity_min=-0.5 * (f.x_max - f.x_min),
        ),
        f,
    )

    print(f.__class__.__name__, pso.simulate(d * 50))
    print(f.__class__.__name__, psovc.simulate(d * 50))
    print(f.__class__.__name__, bpso.simulate(d * 50))
