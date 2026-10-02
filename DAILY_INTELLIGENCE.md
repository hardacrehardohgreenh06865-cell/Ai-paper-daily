# 🤖 Embodied AI & Robotics Frontier Briefing (2026-10-02)

> *Automated Intelligence Briefing generated via custom ETL scoring pipeline. Prioritizes foundation models, manipulation, locomotion, and physical AI systems.*

---

### Top 1: PROMO: Preference-conditioned Multi-Objective Reinforcement Learning for Quadrupedal Robots
- **Priority Score**: `140 pts` | **Published**: `2026-10-01`
- **Focus Tracks**: `#quadruped` `#reinforcement learning` `#locomotion`
- **Key Authors**: Amr Mousa, Rifny Rachman, Neil Karavis et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2610.01260v1) | [PDF Fulltext](http://arxiv.org/pdf/2610.01260v1)

**Executive Abstract**:
> Quadrupedal locomotion requires balancing conflicting objectives such as command tracking, stability, and energy efficiency, yet conventional reinforcement learning (RL) hardcodes these priorities into a fixed scalar reward at training time. We present PROMO (Preference-Conditioned Multi-Objective Reinforcement Learning), a semantic multi-objective approach that makes this trade-off an explicit runtime input to a single locomotion policy. PROMO conditions the policy on deployment facing preferences while keeping embodiment-specific locomotion priors fixed, thereby separating operator intent from reward shaping terms required for viable gait generation. Compared with fixed-objective controllers, multi-objective baselines, and independently trained specialists, PROMO achieves objective specialization and robustness from a single deployable policy. Across 100 sampled preferences in simulation, 67 behaviors are non-dominated under exact Pareto dominance, with a mean preference-objective correlation of 0.843, demonstrating broad Pareto coverage and predictable preference response. The same policy transfers zero-shot to a Unitree Go2, where preference changes alone reduce specific energy by up to 30.4%, position error by 38.7%, and peak body-attitude deviation by 59.0% relative to the balanced preference. These results establish preference-conditioned multi-objective RL as a practical runtime interface for adaptive legged locomotion, extending its role beyond offline Pareto-set construction. Open-source code and videos are available at https://amrmousa.com/promo/.

---

### Top 2: Is Success All You Need? Investigating the Impact of Input Perturbations on VLA Behaviour in Tabletop Manipulation Tasks
- **Priority Score**: `135 pts` | **Published**: `2026-10-01`
- **Focus Tracks**: `#vision-language-action` `#vla`
- **Key Authors**: Sophie Higham, Riccardo Andrea Izzo, Matteo Matteucci et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2610.01351v1) | [PDF Fulltext](http://arxiv.org/pdf/2610.01351v1)

**Executive Abstract**:
> Vision-Language-Action (VLA) models have achieved high task success rates on robot manipulation task benchmarks. More recently, there has been an emphasis on evaluating the robustness of VLA models to perturbations. However, this robustness is still predominantly measured through Task Success Rate (TSR). In this work, we propose a benchmark-agnostic evaluation framework to measure the behavioural robustness of models by characterising how successful trajectories are executed under perturbation. We implement this methodology by extending the widely-used LIBERO and LIBERO-Plus benchmarks. Across three state-of-the-art VLA models, four LIBERO task suites and seven perturbation conditions, we evaluate changes in both typical successful behaviour and its variability, including metrics of motion smoothness, efficiency and gripper behaviour. We find that perturbations can alter the behaviour of successful trajectories, a phenomenon which cannot necessarily be inferred from TSR alone. Across LIBERO suites, we identify cases where state-of-the-art VLA models achieve comparable TSR under the same perturbation condition, yet behaviour on successful trajectories diverges substantially. Therefore, to have a more robust assessment of task performance, we argue that suitable measures of robustness should capture not only whether a task is completed, but also how the robot behaves while completing it. When evaluating the robustness of VLA models, TSR may be complemented by behavioural evaluation metrics that characterise the nature and variability of successful task execution by robots.

---

### Top 3: WBAG: A Whole-Body and Attached-Geometry Safety Framework for Vision-Language-Action Manipulation
- **Priority Score**: `135 pts` | **Published**: `2026-10-01`
- **Focus Tracks**: `#vision-language-action` `#vla`
- **Key Authors**: Samuel Zhen, Siwon Jo, Yanze Zhang et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2610.01083v1) | [PDF Fulltext](http://arxiv.org/pdf/2610.01083v1)

**Executive Abstract**:
> Vision-language-action (VLA) policies have demonstrated impressive capabilities in generalizable robotic manipulation, but their deployment in the real world remains challenging due to potential collisions involving different parts of the robot, manipulated objects, and the surrounding environment. Existing inference-time VLA safety frameworks typically rely on simplified end-effector-centered representations that do not explicitly model the full articulated robot and attached-object geometry. In this paper, we present WBAG, a safety framework that models the robot's whole-body and grasp-dependent attached geometry. WBAG constructs a grasp-conditioned safe set that adapts the protected geometry as objects are grasped, then converts this evolving geometry into differentiable CBF constraints that minimally modify the VLA's native six-dimensional operational-space action for collision avoidance across robot, scene, and attached geometry. On the SafeLIBERO benchmark, a variant of LIBERO augmented with obstacles for safety evaluation, WBAG achieves the best overall safety and safe task success among the evaluated methods under a scene-level safety evaluator that monitors all eligible non-task objects, reaching 97.38\% aggregate Scene Safety and 59.38\% Safe Success.

---

### Top 4: MASkillBlender: Decentralized Whole-Body Coordination for Multi-Humanoid Loco-Manipulation via Skill Blending
- **Priority Score**: `125 pts` | **Published**: `2026-10-01`
- **Focus Tracks**: `#humanoid` `#reinforcement learning`
- **Key Authors**: Yifan Hu, Luhang Hong, Mingkang Long et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2610.01102v1) | [PDF Fulltext](http://arxiv.org/pdf/2610.01102v1)

**Executive Abstract**:
> Coordinated multi-humanoid loco-manipulation is promising yet challenging due to high-dimensional whole-body control, decentralized decision making, and scalability. While recent reinforcement learning methods have improved single-humanoid whole-body control, extending them to the multi-humanoid setting remains nontrivial and often requires substantial reward engineering or task-specific design. We propose MASkillBlender, a general multi-agent reinforcement learning framework to achieve decentralized multi-humanoid whole-body coordination. By learning a shared decentralized high-level policy over reusable pre-trained single-humanoid skills, MASkillBlender enables coordinated behaviors using only task-level rewards, without requiring task-specific motion references. To improve learning efficiency, we further introduce a permutation-based data augmentation strategy for homogeneous multi-humanoid systems, and theoretically show that the permuted samples preserve the policy-gradient direction of the original samples under the homogeneous Markov game formulation. We evaluate MASkillBlender on multiple multi-humanoid coordination tasks across two humanoid embodiments. Simulation results demonstrate that the proposed framework consistently achieves strong task performance and enables coordinated behaviors across different tasks and humanoid embodiments.

---

### Top 5: FutureWorlds: Learning Robotic World Models from Alternative Futures
- **Priority Score**: `120 pts` | **Published**: `2026-10-01`
- **Focus Tracks**: `#world model` `#reinforcement learning`
- **Key Authors**: Hao Wu, Shengju Qian, Weiyan Wang et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2610.01019v1) | [PDF Fulltext](http://arxiv.org/pdf/2610.01019v1)

**Executive Abstract**:
> Robotic world models predict action-conditioned future scenes, providing a foundation for understanding action outcomes. However, turning alternative predictions into useful learning signals remains challenging: similar candidates limit informative quality comparisons, while diverging trajectories require persistent maintenance of their individual histories. We introduce FutureWorlds, a framework that unifies candidate construction, history maintenance, and learning from relative quality. Built on a multimodal discrete autoregressive model, FutureWorlds uses diverse beam search during reinforcement learning to construct candidate futures that balance confidence and diversity. Candidate-specific bounded memory preserves scene states and ensures that generation and policy scoring use matching histories. We further propose MemSPO (Memory-Conditioned Search-Guided Policy Optimization), which converts video trajectory rewards into group-relative advantages to optimize the world model. On RT-1, BridgeV2, and RoboCasa, FutureWorlds reduces LPIPS for 32-frame predictions by 14.78%, 20.84%, and 9.12%, respectively, relative to the strongest baseline on each dataset. Under fixed evaluation configurations, only 200 MemSPO updates further improve generation quality and support continued prediction beyond the training horizon. Memory ablations, decoding sensitivity analysis, and optical-flow evaluation show that these gains extend beyond visual quality to more accurate motion prediction and more consistent object states. Project page and code: https://github.com/Alexander-wu/FutureWorlds.

---

