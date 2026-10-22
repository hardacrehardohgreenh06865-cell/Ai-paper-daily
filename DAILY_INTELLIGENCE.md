# 🤖 Embodied AI & Robotics Frontier Briefing (2026-10-22)

> *Automated Intelligence Briefing generated via custom ETL scoring pipeline. Prioritizes foundation models, manipulation, locomotion, and physical AI systems.*

---

### Top 1: From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent Manipulation
- **Priority Score**: `135 pts` | **Published**: `2026-10-21`
- **Focus Tracks**: `#vision-language-action` `#vla`
- **Key Authors**: Tingwen Du, Haoyu Guo, Hanxue Zhang et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2610.29560v1) | [PDF Fulltext](http://arxiv.org/pdf/2610.29560v1)

**Executive Abstract**:
> Vision-language-action (VLA) models achieve strong performance across embodied manipulation tasks by unifying visual understanding, language conditioning, and action generation. However, long-horizon tasks can involve non-Markovian dependencies: successful decisions may require retaining task progress and past interaction outcomes, while partial observability and execution errors compound over time. Existing work has begun to address these challenges by augmenting foundation-model policies with memory and by introducing hierarchical architectures that separate high-level planning from low-level execution. We organize the high-level VLM as a robotic agent through an editable harness to maintain task context and improve planning through execution experience. We instantiate this approach as SERA (Self-Evolving Robotic Agent), with a fixed VLA executor providing low-level control. The harness maintains and updates task context using observations and execution feedback to guide subsequent planning. Self-evolution uses environment rollouts to propose and evaluate harness revisions, with the selected configuration fixed before held-out testing. On RoboMME, SERA achieves 51.38% overall success with autonomous selection, compared with 44.38% without self-evolution. Our exploration suggests that agentic planning is a promising direction for history-dependent robotic manipulation.

---

### Top 2: Plan First, Act Later: Streaming Reasoning for Executable Memory in Robot Control
- **Priority Score**: `135 pts` | **Published**: `2026-10-21`
- **Focus Tracks**: `#vision-language-action` `#vla`
- **Key Authors**: Qinghang Liu, Conglin Wang, Zongsheng Li et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2610.29329v1) | [PDF Fulltext](http://arxiv.org/pdf/2610.29329v1)

**Executive Abstract**:
> Long-horizon robot manipulation requires a robot to remember task-relevant information beyond its short observation window. Existing memory-augmented policies typically retrieve relevant information from history and reason over it at execution time, placing a heavy reasoning burden on the high-level model. To address this challenge, we propose PAL (\textbf{P}lan first, \textbf{A}ct \textbf{L}ater), a hierarchical memory framework for vision-language robot manipulation. It maintains a short-term visual buffer, a semantic-event memory, and an executable \texttt{subtask\_list}. A high-level vision-language model (VLM) converts streaming visual observations into the \texttt{subtask\_list}. At execution time, the VLM selects the currently relevant subtask from the \texttt{subtask\_list} and passes it to a low-level vision-language-action (VLA) policy. To teach the model what to write to memory and when to update it, we introduce a two-stage data generation procedure that first expands sparse update supervision and then uses self-labeling with task-grounded verification to generate training data that better match the state distribution encountered during execution. We evaluate our approach on memory-dependent benchmarks and real-world manipulation tasks. On RoboMME, PAL achieves a \textbf{56.05\%} success rate, outperforming the strongest baseline, FrameSamp-Modul, at 44.51\%. In real-world experiments across four manipulation tasks, \pal{} reaches \textbf{60.83\%} overall success, surpassing MemER (45.00\%) and FrameSamp-Modul (28.33\%). These results show that proactively writing future-relevant subtasks into hierarchical memory improves long-horizon visual reasoning and robot control. Code and videos can be found on our website: https://qinghangliu.github.io/pal-webpage/

---

### Top 3: End-to-End Reinforcement Learning for Quadrupedal Jumping in Lunar Gravity
- **Priority Score**: `115 pts` | **Published**: `2026-10-21`
- **Focus Tracks**: `#quadruped` `#reinforcement learning`
- **Key Authors**: Levin Müller, Oliver Fischer, Marco Trentini et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2610.29586v1) | [PDF Fulltext](http://arxiv.org/pdf/2610.29586v1)

**Executive Abstract**:
> Legged robots can extend planetary exploration to rugged and discontinuous terrain that is inaccessible to conventional rovers. In lunar gravity, jumping further expands this mobility by enabling robots to cross obstacles and gaps that cannot be traversed by walking alone. We present a multistage reinforcement-learning approach that produces a single end-to-end control policy for commanded point-to-point jumping under lunar gravity. The resulting policy has a simple architecture and relies exclusively on mission-compatible onboard sensing, making its deployment on a real lunar mission plausible. In simulation, the learned policy performs accurate point-to-point jumps with landing errors smaller than the robot's body size. We analyze the torque and power demands of lunar jumping and characterize performance degradation under extreme outlier events, including control-update freezes of up to \SI{1}{s} during flight. Hardware transfer demonstrates that the policy can successfully execute a vertical jump under lunar-gravity offloading. Furthermore, the measured torque and power profiles are consistent with the simulation results and remain within the robot's hardware limits.

---

### Top 4: A2I-Calib++: A Kinematics-Driven Anti-noise Active Calibration Framework for Whole-Body Multi-IMU Systems on Legged Robots
- **Priority Score**: `110 pts` | **Published**: `2026-10-21`
- **Focus Tracks**: `#quadruped` `#locomotion`
- **Key Authors**: Fangyu Jiang, Chaoran Xiong, Kehui Ma et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2610.29438v1) | [PDF Fulltext](http://arxiv.org/pdf/2610.29438v1)

**Executive Abstract**:
> Recently, multi-node inertial measurement unit (multi-IMU) systems have shown promise for robust odometry in legged robots. Multi-IMU fusion can improve legged robot odometry but requires accurate spatiotemporal calibration among the sensors. Existing multi-IMU calibration methods, designed for aerial or handheld platforms, face challenges on legged robots because routine locomotion may provide insufficient excitation, while foot slips, impacts, and vibrations introduce measurement disturbances. To address these challenges, we propose A2I-Calib++, a kinematics-driven anti-noise active calibration framework for body-mounted IMUs covered by the robot kinematic model. It estimates temporal offsets, extrinsic rotations and translations, and inertial biases through temporal correlation search followed by analytic spatial and bias estimation, without artificial calibration targets or complex parameter tuning for the target IMU. A2I-Calib++ comprises three core modules: 1) a Noise-Isotropy-Inspired Trajectory supported by a finite-horizon conditioning proposition that generates sufficient excitation to limit noise sensitivity; 2) a constraint-aware Adversarial Motion Priors controller that combines the anti-noise excitation with a rolling-contact reward for contact-aware execution; and 3) a contact-constrained virtual IMU that fuses pre-calibrated calf IMUs and joint kinematics under a rolling-contact model to construct the calibration reference. Furthermore, evaluations on both simulation and real-world quadruped platforms demonstrate notably reduced noise sensitivity and simulation calibration errors compared to conventional methods, together with repeatable real-world calibration and improved proprioceptive odometry accuracy for legged robots.

---

### Top 5: Make it Walk: Computational Design of LEGO Walkers
- **Priority Score**: `95 pts` | **Published**: `2026-10-21`
- **Focus Tracks**: `#locomotion` `#actuator`
- **Key Authors**: Siqi Li, Fancheng Gao, Chi-Wing Fu et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2610.29505v1) | [PDF Fulltext](http://arxiv.org/pdf/2610.29505v1)

**Executive Abstract**:
> LEGO walkers are walking automata constructed from modular LEGO Technic bricks. They exhibit intriguing locomotion and are also highly reconfigurable through the modular Technic bricks, making them widely applicable in education, recreation, and robotics research. However, existing LEGO walkers are designed mostly by reusing existing single-actuator walking mechanisms. Although the locomotion is stable, their fixed walking gaits limit their adaptability and versatility. This paper presents the first computational solution capable of designing LEGO walkers that not only walk stably, but also support a variety of walking gaits. Our idea is twofold. First, we control the foot motion trajectory of each leg mechanically via a specifically-designed gear-linkage mechanism, in which we incorporate a pair of 3D-printed non-circular gears to work with a LEGO Technic mechanism. Second, we drive each leg by an independent motor and synchronize the timings of multiple leg motions via a simple yet adaptable control algorithm, enabling stable and versatile locomotion. Importantly, we take this modeling as a foundation to co-design the morphology and control of the LEGO walkers to meet the target locomotion and appearance. Leveraging our approach, we created a variety of LEGO walkers, demonstrating various walking gaits and appearances, and fabricated some of them to show their locomotion capability in the real world.

---

