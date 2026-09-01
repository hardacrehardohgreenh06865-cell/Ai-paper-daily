# 🤖 Embodied AI & Robotics Frontier Briefing (2026-09-01)

> *Automated Intelligence Briefing generated via custom ETL scoring pipeline. Prioritizes foundation models, manipulation, locomotion, and physical AI systems.*

---

### Top 1: Blind Dexterity: Whole-Body Humanoid Manipulation via Pure Proprioception
- **Priority Score**: `160 pts` | **Published**: `2026-08-30`
- **Focus Tracks**: `#humanoid` `#bipedal` `#dexterous manipulation`
- **Key Authors**: Aditya Bhatt, Oleg Kaidanov, Puze Liu et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2608.29487v1) | [PDF Fulltext](http://arxiv.org/pdf/2608.29487v1)

**Executive Abstract**:
> We present blind, whole-body manipulation skills on a Unitree G1 humanoid using only onboard proprioception, without cameras, markers, force-torque, or tactile sensors. Despite this minimal sensing, the trained policies exhibit surprising capability across qualitatively different tasks: push-resilient bipedal walking without IMU feedback, active soccer ball trapping with a foot, seeking and lifting a suitcase by its handle, and mounting a randomly positioned skateboard. We argue that these capabilities arise from a key underappreciated signal: the way the joint encoder readouts evolve under purposeful compliant contact, effectively forming a whole-body tactile channel. By generating contact-rich motions, the trained policies actively probe the environment; as a result, task-relevant object state (e.g., pose) becomes increasingly decodable from short proprioceptive histories. We expose this information using compact task-specific state estimators trained alongside, but fully separately from, the policies; their prediction errors decrease rapidly after informative contact. Our results indicate that joint encoder-based proprioception, combined with compliant actuation (now widely available on commercial robots and low-cost motors) is already a strong, practical substrate for whole-body dexterous manipulation and interactive perception, and therefore a natural foundation on which richer sensing can be layered.

---

### Top 2: AGM: Achievement-Grounded Memory for Closed-Loop Agents with Frozen VLA Policies
- **Priority Score**: `135 pts` | **Published**: `2026-08-30`
- **Focus Tracks**: `#vision-language-action` `#vla`
- **Key Authors**: Hongbo Gao, Zeyu Ni, Xin Wen et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2608.29537v1) | [PDF Fulltext](http://arxiv.org/pdf/2608.29537v1)

**Executive Abstract**:
> Frozen vision-language-action (VLA) policies offer broad manipulation skills but execute open-loop action chunks without tracking task progress, so the agent cannot reliably decide whether to continue, retry, or terminate. External memory is a natural remedy, yet it can be harmful when attempted actions are treated as completed progress, turning local execution errors into persistent task-state errors. We propose Achievement-Grounded Memory (AGM), a lightweight closed-loop framework for frozen VLA policies that represents a task as a subgoal sequence with a progress pointer and advances this memory only after the current subgoal is verified by physical evidence. Proprioceptive interaction cues decide when to verify, while coherent point tracking and language-conditioned cross-view comparison, sourced from frozen foundation models through a single 2.43M-parameter verification head, decide what was achieved. AGM thereby converts open-loop execution into a closed loop of execution, verification, and progress, keeping the policy frozen without test-time large-model inference. On the RoboMME Counting benchmark, AGM reaches on PickXTimes and on BinFill, surpassing the strongest memory-augmented baseline by points on average, and the framework yields equally decisive gains on a physical robot. Reliable embodied memory thus depends more on disciplined state updates than on memory capacity.

---

### Top 3: SMILE: Smooth Motion for Improved Long-Horizon VLA Execution
- **Priority Score**: `135 pts` | **Published**: `2026-08-29`
- **Focus Tracks**: `#vision-language-action` `#vla`
- **Key Authors**: Jongwoo Park, E-Ro Nguyen, Kanchana Ranasinghe et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2608.29432v1) | [PDF Fulltext](http://arxiv.org/pdf/2608.29432v1)

**Executive Abstract**:
> Vision-Language-Action (VLA) models reduce inference cost by executing multiple actions per call, but longer horizons often degrade accuracy because raw chunks contain jitter and outliers. We introduce SMILE, an architecture-preserving interface that predicts B-spline coefficients and decodes them into smooth action sequences. SMILE changes only the action representation, enabling longer fixed horizons while retaining each baseline's backbone and model scale. We apply SMILE to SmolVLA, Evo1, VPP, and DAWN, improving accuracy and amortized inference efficiency across LIBERO, CALVIN, and real-world experiments. SMILE-Evo1 reaches 98.0% with a 1.1x speedup on LIBERO, while SMILE-VPP reaches an average length of 4.42 with a 1.5x speedup on CALVIN. At a matched execution horizon of 10, SMILE-SmolVLA reduces non-boundary acceleration by 78.6% and velocity sign-change rate by 42.3%. Real-world xArm tests show higher success, fewer drops, and fewer contacts. These results establish smooth coefficient-space generation as a route to accurate, efficient long-horizon VLA execution. Project page: jongwoopark7978.github.io/smilevla

---

### Top 4: AnyWorld: Factorized Egocentric World Models for Cross-Embodiment Generalization
- **Priority Score**: `135 pts` | **Published**: `2026-08-29`
- **Focus Tracks**: `#humanoid` `#world model`
- **Key Authors**: Cheng Chen, Jerry Bai, Jiacheng Wei et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2608.29242v1) | [PDF Fulltext](http://arxiv.org/pdf/2608.29242v1)

**Executive Abstract**:
> Collecting contact-rich robot experiences at scale remains a major bottleneck for generalizable manipulation. Beyond data quantity, robot learning also requires diverse experiences across embodiments, viewpoints, and scenes. Human egocentric videos provide abundant physical interactions, but each video captures only a narrow slice of experience under a single body, camera trajectory, and environment. We propose AnyWorld, a cross-embodiment world modeling framework that expands a single human interaction into diverse robot-native rollouts without paired human-robot demonstrations. Our model factorizes an interaction into action, camera, and embodiment: action controls capture the motion structure, camera controls specify viewpoint evolution, and the target embodiment context defines the acting body and its interaction geometry. This formulation enables independent recomposition of embodiment, viewpoint, and scene factors, allowing a single model to generate many robot-domain experiences while preserving the underlying dynamics and object interactions. We train the model with large-scale human interaction pretraining followed by mixed-embodiment fine-tuning. Experiments show that our model supports controllable recomposition across embodiments, viewpoints, and scenes, and we further demonstrate that the generated data can improve manipulation performance on the RoboCasa GR1 tabletop benchmark and a real IRON humanoid robot. Beyond aggregate gains, we test whether unpaired human experience can be recomposed into robot-native video-action pairs that target a policy gap. Controlled IRON interventions correct a spurious completion prior and establish language-grounded spatial target selection; an action-only counterfactual intervention fails to learn the latter reliably, showing that both action calibration and visual recomposition are necessary.

---

### Top 5: $\mathcal{N}_0$-Foundation: Towards the Age of Tactile Intelligence
- **Priority Score**: `100 pts` | **Published**: `2026-08-30`
- **Focus Tracks**: `#tactile sensing` `#teleoperation`
- **Key Authors**: NeoteAI Team, Fudan TEAI Team
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2608.29601v1) | [PDF Fulltext](http://arxiv.org/pdf/2608.29601v1)

**Executive Abstract**:
> We present $\mathcal{N}_0$-Foundation, a paradigm for tactile-enabled embodied manipulation, which integrates tactile sensing hardware, large-scale multimodal data, tactile representation learning, and standardized evaluation. First, we engineer the infrastructure for scalable data collection, including a vision-based tactile sensor, a tactile Universal Manipulation Interface (UMI), and a synchronized visuo-tactile data collection system supporting both robot embodiments and UMI-based demonstrations. Leveraging this infrastructure, we construct NeoData, which contains more than 30000 hours of synchronized visual and tactile demonstrations, spanning six embodiments, 450 tasks, and billions of paired RGB and tactile frames collected through a mixture of real-robot teleoperation and UMI-based demonstrations. To facilitate open research, we further release OpenNeoData, a 5000-hour open-source subset of NeoData. The dataset addresses a central limitation of existing manipulation corpora, critical for deformable-object manipulation, precise assembly, delicate force control, and sustained surface interaction. Capitalizing on the large-scale, heterogeneous tactile measurements, we propose NeoForce, a visuo-tactile representation model that learn transferable tactile representations across different sensor designs. To enable systematic evaluation of tactile embodied models built upon our infrastructure, datasets and tactile representations, we further propose a comprehensive benchmark, which combines the real-world NeoReal suite and the simulated NeoSim suite for standardized evaluation. Experiments across both suites show that policies benefit from the physical contact state rather than from the device-specific appearance of the tactile signal. We release the dataset, the representation, and the benchmark, aiming at supporting future work on tactile-enabled embodied manipulation.

---

