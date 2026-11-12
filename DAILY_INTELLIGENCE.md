# 🤖 Embodied AI & Robotics Frontier Briefing (2026-11-12)

> *Automated Intelligence Briefing generated via custom ETL scoring pipeline. Prioritizes foundation models, manipulation, locomotion, and physical AI systems.*

---

### Top 1: Koopman Model-Based Reinforcement Learning
- **Priority Score**: `175 pts` | **Published**: `2026-11-10`
- **Focus Tracks**: `#bipedal` `#quadruped` `#reinforcement learning` `#locomotion`
- **Key Authors**: Wenjian Hao, Paulo C. Heredia, Shaoshuai Mou
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2611.14186v1) | [PDF Fulltext](http://arxiv.org/pdf/2611.14186v1)

**Executive Abstract**:
> We propose a Koopman model-based reinforcement learning (K-MBRL) algorithm for controlling nonlinear robotic systems with unknown dynamics. The K-MBRL learns a control policy by minimizing an approximate policy objective that combines the analytical immediate cost with an estimate of the future cost evaluated at the one-step predicted state. To this end, we develop a stochastic Koopman operator-based learning method to approximate the unknown nonlinear dynamics in a linear representation, while a critic function estimates the remaining future cost. This formulation offers two key advantages. First, the linear Koopman dynamics simplify the model-dependent policy gradient computation to a constant matrix product, enabling computationally efficient policy improvement. Second, one-step model propagation mitigates the accumulation of prediction errors associated with long-horizon rollouts while retaining long-term cost information through the critic. The learned policy enables real-time control through feedforward evaluation without online optimization. We establish policy learning convergence guarantees under standard stochastic approximation assumptions. Simulations on HalfCheetah and quadruped four-legged locomotion tasks demonstrate strong sample efficiency and improved performance compared with classical model-free and model-based reinforcement learning baselines. A pendulum swing-up task is used to assess policy gradient approximation accuracy and conduct ablation studies on the learning mechanism and key hyperparameters. The proposed K-MBRL is further validated on a physical quadruped robot performing a challenging sequence of maneuvers: rising to an upright posture supported by two rounded rear feet, maintaining balance during bipedal walking, and safely returning to the ground, as shown in Fig.1.

---

### Top 2: One Policy for 100 Household Tasks: Our Solution for the 2026 BEHAVIOR Challenge
- **Priority Score**: `155 pts` | **Published**: `2026-11-10`
- **Focus Tracks**: `#vision-language-action` `#vla` `#teleoperation`
- **Key Authors**: Ilia Larchenko, Gleb Zarin, Atindra Nair et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2611.14432v1) | [PDF Fulltext](http://arxiv.org/pdf/2611.14432v1)

**Executive Abstract**:
> We describe our solution for the 2026 BEHAVIOR Challenge: 100 long-horizon household tasks in the OmniGibson simulator. We placed 9th on the final leaderboard, the only independent team in the top 10. The core of the solution is a single vision-language-action (VLA) model, one checkpoint for all 100 tasks, built on our 1st-place 2025 solution, which is based on $π_{0.5}$. On the 50 tasks shared with 2025, its Q rises from 0.260 to 0.371; across all 100 tasks it scores 0.392. Our main conclusion from 2025 was that the model was undertrained, so most of the 2026 work went into training the model for longer, optimizing some training parameters, making each training step slightly faster and reducing the gradient noise: a migration from 50 to 100 tasks (semantic stages built from the demonstrations' skill annotations, task and stage embeddings of new tasks warm-started from similar old ones, and a 21-dimensional action space matching the teleoperation controls); variance-reduced multi-sample flow matching with a simple noise-vs-compute model that picks the number of action-expert samples per observation without ablations; and a 200k-step training run, about one pass over the 211M frames of the demonstrations. A cloud evaluation infrastructure keeps a shared record with provenance, episode diagnostics and restorable simulator states, and runs six simulators on one GPU together faster than real time. On top of the learned policy, 14 tasks are routed to a GPT-6 Astra coding agent that controls the robot through observation and motion tools, starting every episode from a frozen copy of its own practice session on training instances. Across these 14 tasks, Astra's mean Q is 0.639, against 0.108 for the learned policy. The public submission included only part of the Astra results and scored 0.446 Q with 27.3% full-task success.

---

### Top 3: Is Your Robot's Memory Just a Clock? Temporal Shortcuts in Memory-Augmented VLA Policies
- **Priority Score**: `135 pts` | **Published**: `2026-11-10`
- **Focus Tracks**: `#vision-language-action` `#vla`
- **Key Authors**: Chubin Zhang, Bo An
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2611.14488v1) | [PDF Fulltext](http://arxiv.org/pdf/2611.14488v1)

**Executive Abstract**:
> Memory-augmented vision-language-action (VLA) policies are meant to remember what happened. Many of them, however, fill memory by time: they sample frames uniformly across the episode and stamp each frame with its time step. Because time passes even when nothing happens, such a memory may not tell waiting from working. We show that it does not. On the counting tasks of RoboMME, we make the robot briefly pause or fidget its wrist. Such a null event changes nothing the task depends on, yet a released memory VLA counts the interval as work done and stops early. We call this failure phantom progress. It cuts success from 47 to 16 of 50 on one task and from 44 to 10 on the other. When the same frames are withheld from memory, success returns, so the cause lies in memory rather than in the interruption itself. We trace the failure to a temporal shortcut: because demonstrations proceed at a steady pace, elapsed time predicts progress. Indeed, rescaling the time stamps alone makes the policy stop early when the clock runs fast and repeat when it runs slow. Surprisingly, removing the time encoding does not cure the failure, because the frames of a null event still occupy slots of the time-sampled memory. Across RoboMME's released designs, vulnerability follows how memory is indexed. Of the fixes the diagnosis suggests, training with injected pauses does not remove the failure and impairs counting, whereas indexing memory by events recovers half or more of the loss without retraining. A memory meant to remember what happened should count events rather than clock ticks.

---

### Top 4: DexSeed: Expanding Human Hand-Object Interactions into Robot Demonstrations for Dexterous Policy Learning
- **Priority Score**: `135 pts` | **Published**: `2026-11-10`
- **Focus Tracks**: `#vision-language-action` `#vla`
- **Key Authors**: Huaijin Pi, Zehong Shen, Yong Wang et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2611.14092v1) | [PDF Fulltext](http://arxiv.org/pdf/2611.14092v1)

**Executive Abstract**:
> We study how to generate diverse, physically executable robot demonstrations for dexterous vision-language-action (VLA) learning. Existing demonstration-generation methods typically rely on costly teleoperated examples. Meanwhile, human hand--object datasets provide a reusable source, but existing transfer methods mainly reproduce given interactions. Turning these interactions into VLA training data further requires coverage of different objects and manipulation locations, together with executable arm and finger actions, and visual observations. To achieve this, we present DexSeed, a framework for low-cost generation of dexterous robot data from human hand--object interactions. Our key idea is to expand human sequences while preserving their grasps and realizing the resulting motions under arm-tracking dynamics in physics simulation. Specifically, we organize source sequences by grasp mode with shared language descriptions. InteractionMesh-based retargeting and arm trajectory augmentation adapt these sequences to the robot hand, different object geometries, and pick-and-place locations while preserving local hand--object relationships. An RL finger-control policy produces executable rollouts, while the arm tracks precomputed trajectories. Rendered observations and recorded actions from successful rollouts are paired with grasp descriptions to fine-tune a VLA. Experiments show improved contact fidelity in retargeting and more reliable whole-arm execution than the evaluated baselines. Simulation evaluation and real-world deployment further demonstrate that a VLA fine-tuned solely on the generated demonstrations can execute language-specified grasps. Project page: https://robbyant-research.github.io/DexSeed/.

---

### Top 5: LaST0.5: A Generalist World Action Model with Interaction-Centric Latent Reasoning
- **Priority Score**: `120 pts` | **Published**: `2026-11-10`
- **Focus Tracks**: `#world model` `#dexterous manipulation`
- **Key Authors**: Xuheng Zhang, Yiming Zhang, Jialin Gao et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2611.14048v1) | [PDF Fulltext](http://arxiv.org/pdf/2611.14048v1)

**Executive Abstract**:
> World Action Models (WAMs) have recently emerged as a promising paradigm for robotic manipulation, endowing policies with strong capabilities for modeling temporal and physical dynamics. Existing WAMs, encompassing both video-first action prediction and joint video-action modeling, directly transfer global physical representations from world models to action generation. However, global scene representations may underemphasize local robot-object interactions, creating a mismatch between representations optimized for world evolution and those required for manipulation. To bridge this gap, we propose LaST0.5, a novel WAM that introduces an interaction-centric physical representation between world modeling and action generation. Specifically, LaST0.5 learns a compact interaction-centric latent space under the supervision of visual interaction cues between the robot and the environment. This reasoning space is instantiated as a latent expert that bridges the world expert and the action expert within a Mixture-of-Transformers architecture. Furthermore, LaST0.5 performs adaptive world-to-action transfer by jointly predicting future representations and progress values, using progress consistency to adjust action execution and trigger future resampling. Finally, we pretrain LaST0.5 on a large-scale robotic data corpus comprising over 14k hours of data, establishing interaction-centric physical reasoning as a scalable and effective paradigm. LaST0.5 achieves 99.5% on LIBERO, surpasses the previous state of the art on ten evaluated RLBench tasks, and demonstrates robust long-horizon execution and precise dexterous manipulation in real-world experiments.

---

