# 🤖 Embodied AI & Robotics Frontier Briefing (2026-11-13)

> *Automated Intelligence Briefing generated via custom ETL scoring pipeline. Prioritizes foundation models, manipulation, locomotion, and physical AI systems.*

---

### Top 1: PolyMorphWBC: Whole-Body Control from End-Effector Trajectories for Quadrupedal Mobile Manipulation across Arm Morphologies with Extended Reach
- **Priority Score**: `195 pts` | **Published**: `2026-11-11`
- **Focus Tracks**: `#quadruped` `#locomotion` `#vision-language-action` `#vla`
- **Key Authors**: Heng Li, Yang Li, Yifan Duan et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2611.15117v1) | [PDF Fulltext](http://arxiv.org/pdf/2611.15117v1)

**Executive Abstract**:
> Quadrupedal mobile manipulators can extend their manipulation workspace by coordinating the mounted arm with the mobile base. At the task level, short-horizon end-effector (EE) trajectories provide an interface for specifying the desired manipulation motion without prescribing how it should be realized by the arm and base. However, executing such trajectories remains challenging because the controller must determine when and how the base should move, and this decision depends on the mounted-arm morphology. We therefore present PolyMorphWBC, a hierarchical controller that takes an EE trajectory as the sole task-level motion command and generates coordinated arm--base motions across four families of 6-DoF mounted arms, with extended-reach trajectories beyond the initial fixed-base reach. Within PolyMorphWBC, a trajectory-conditioned coordinator determines the base motion from previewed EE targets, while arm-specific Inverse Kinematics (IK) tracks the current target, and a frozen locomotion backend executes the resulting motion. Cross-arm reuse is enabled by a Unified Robot Description Format (URDF)-derived morphology conditioning, together with online residual-wrench feedback. We train PolyMorphWBC on procedurally generated arms and structured trajectories within and beyond fixed-base reach. In IsaacLab, it achieves 93.95% completion with 2.30cm position error and 4.81° orientation error on held-out trajectories and arm morphologies. In MuJoCo evaluation against UMI-on-Legs, PolyMorphWBC reduces EE position error by 69--72% and orientation error by 91--97% across four within- and extended-reach trajectories. On a physical Go2--ARX5 system, we demonstrate language-conditioned extended-reach pick-and-place using EE trajectories from pi_0 without vision-language-action (VLA)-generated base commands.

---

### Top 2: What Makes a VLA Reactive? A Study of Execution Strategies for Dynamic Manipulation
- **Priority Score**: `165 pts` | **Published**: `2026-11-11`
- **Focus Tracks**: `#reinforcement learning` `#vision-language-action` `#vla`
- **Key Authors**: Zhuoyue Li, Zhendong Han, Pankhuri Vanjani et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2611.15491v1) | [PDF Fulltext](http://arxiv.org/pdf/2611.15491v1)

**Executive Abstract**:
> Vision-language-action (VLA) models predict chunks of future actions, and when objects move, those chunks go stale before they are executed. We study what makes a pretrained VLA reactive, using \pihalf{} on two dynamic simulation benchmarks and three real-robot tasks. We vary the prediction and execution horizons, compare synchronous and asynchronous inference, test methods that deliver actions sooner or keep successive chunks continuous, and adapt the policy with motion cues and latent-space reinforcement learning. The best prediction horizon is about one second, and the best execution horizon depends on the checkpoint. Short horizons help more with asynchronous execution, and methods that keep the trajectory continuous outperform those that only reduce latency. Adapting the policy repairs targeted failures, but on the conveyor task changing the execution horizon gained as much. Reactivity depends on the execution pipeline as much as on the policy, so both should be evaluated together.

---

### Top 3: AFTER: A World Model with Adaptive Fast--Slow Timescales for Error-Driven Retention
- **Priority Score**: `140 pts` | **Published**: `2026-11-11`
- **Focus Tracks**: `#embodied ai` `#world model`
- **Key Authors**: Haoyi Zhang, Qi Zhang, Yunfan Ren et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2611.15215v1) | [PDF Fulltext](http://arxiv.org/pdf/2611.15215v1)

**Executive Abstract**:
> In robotics and embodied AI, a core challenge for world models is adapting to sudden, persistent, yet initially unknown changes in robot dynamics during interaction. For instance, when a robotic arm grasps an object with an unknown payload, the robot dynamics change suddenly. If the world model fails to adapt, its prediction errors accumulate over the open-loop rollout and ultimately mislead the robot's actions. Existing world models, however, struggle to simultaneously satisfy three critical requirements for dynamics adaptation: responsiveness, reacting promptly to sudden changes to curb prediction error accumulation; stability, distinguishing persistent changes from transient disturbances to prevent incorrect updates; and persistence, retaining the adapted dynamics without new observations so that later predictions do not revert to the old dynamics. Inspired by predictive coding in the human brain with multi-timescale adaptation, we propose AFTER-WM, a world model with Adaptive Fast-slow Timescales for Error-driven Retention, whose prediction errors drive a fast correction that fades and a slow correction that persists, while dynamically adjusting the combination weights of pre-trained experts without altering them, to overcome the trade-offs among responsiveness, stability and persistence. On five simulated robot datasets and real UAV data, AFTER-WM has a lower multi-step mean error than all ten compared models and the highest mean return in a joint-failure control task. In simulation, its multistep mean error is 16%-34% below the strongest compared model's and is also the lowest 1-4 steps after a change and under transient disturbances alone, and its step-40 error is the lowest as well, reflecting responsiveness, stability and persistence. All code (method, baselines, experiments) and datasets will be released online.

---

### Top 4: Low-Cost Mobile Bimanual Manipulation for Long-Horizon Toilet Cleaning
- **Priority Score**: `135 pts` | **Published**: `2026-11-11`
- **Focus Tracks**: `#vision-language-action` `#vla`
- **Key Authors**: Sven Schreiber, Bernard Burdiek, Lasse Huber-Saffer et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2611.15381v1) | [PDF Fulltext](http://arxiv.org/pdf/2611.15381v1)

**Executive Abstract**:
> Vision-Language-Action (VLA) models have shown promising capabilities for robot manipulation, but their performance on accessible mobile bimanual platforms remains underexplored. We present a low-cost and reproducible mobile bimanual platform integrating two LeRobot SO-101 manipulators with a TurtleBot 4 and a LeRobot-ROS 2 software stack. Using long-horizon toilet cleaning as a case study, we collect 250 real-world demonstrations and evaluate $π_0$, $π_{0.5}$, SmolVLA, and GR00T under the same embodiment and task conditions. We further evaluate variants using SARM-derived task-progress signals and short-term MEM observation history. Among the evaluated models, $π_0$ performs best, achieving 60% strict and 70% relaxed autonomous success, increasing to 90% with limited human intervention. In contrast, the evaluated progress- and memory-augmented variants do not improve their corresponding baselines. Our results demonstrate the feasibility of long-horizon mobile bimanual manipulation on accessible hardware while highlighting remaining challenges in reliable VLA deployment. Project website: https://so101-turtlebot4.github.io/mobile-bimanual-cleaning/

---

### Top 5: Elastra: A Simulation Framework for Elastic Bodies
- **Priority Score**: `125 pts` | **Published**: `2026-11-11`
- **Focus Tracks**: `#humanoid` `#reinforcement learning`
- **Key Authors**: Youran Sun, Chugang Yi, Xingyu Ren et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2611.15112v1) | [PDF Fulltext](http://arxiv.org/pdf/2611.15112v1)

**Executive Abstract**:
> When robots interact with elastic surfaces such as mattresses and trampolines, changes in loading cause the surfaces to deform and rebound, altering subsequent contact locations and forces. We present Elastra, a simulation framework for modeling this interaction and supporting the training and evaluation of robot control policies. Elastra represents each surface using elements that move only vertically, with elastic connections and damping to model deformation and recovery. Contact forces drive surface motion, and the updated surface geometry is used to compute subsequent contact forces. We systematically validate our simulations against an independent implementation and a real mattress load curve. We further use Elastra to train the Unitree G1 humanoid to stand up on mattresses and trampolines. Using the pretrained HoST policy and ProtoMotions motion tracker as original controllers, we train residual policies through reinforcement learning to add corrections to their joint targets. Adding these residual policies increases the success rate with HoST from 44.1\% to 72.5\%, and from 55\% to 89\% on the trampoline. With ProtoMotions, the success rate increases from 19.0\% to 45.0\% for initial poses not encountered during training. The code and video are available on https://github.com/yichg/elastra.

---

