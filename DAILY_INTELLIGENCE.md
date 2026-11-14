# 🤖 Embodied AI & Robotics Frontier Briefing (2026-11-14)

> *Automated Intelligence Briefing generated via custom ETL scoring pipeline. Prioritizes foundation models, manipulation, locomotion, and physical AI systems.*

---

### Top 1: FORGE: Force-Aware Multi-Granularity Control for Efficient Humanoid Loco-Manipulation
- **Priority Score**: `120 pts` | **Published**: `2026-11-12`
- **Focus Tracks**: `#humanoid` `#locomotion`
- **Key Authors**: Liangjun Xing, Ke Fan, Kailin Li et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2611.17142v1) | [PDF Fulltext](http://arxiv.org/pdf/2611.17142v1)

**Executive Abstract**:
> Humanoid loco-manipulation requires coordinated locomotion, balance regulation, and manipulation under frequent contacts, making teleoperated demonstration collection difficult: a practical controller must simultaneously provide precision, stability, and contact awareness. We propose FORGE, a force-aware multi-granularity control system with a coarse-to-fine command space spanning velocity navigation, planar foot placement, wrist-pose tracking, and optional force-conditioning inputs. Policy training requires no full-body human motion trajectories or joint-angle references; deployment consumes only sparse bilateral wrist poses relative to the pelvis, coarse motion commands, and optional desired wrist-load inputs. For sustained contact, FORGE combines a momentum observer with a learned correction trained using simulator contact-force supervision. At deployment, it estimates low-frequency, wrist-equivalent interaction forces from proprioception and reconstructed low-level arm PD torques, without wrist force/torque sensors. A quasi-static virtual-target loop uses this estimate and an optional desired applied-force input to adapt the wrist target. A frozen locomotion prior and asymmetric residual actions stabilize manipulation-induced whole-body corrections. Experiments evaluate unified-control stability, task-space tracking, quasi-static wrist-equivalent force estimation, squeezing forces during sustained contact with a rigid box, and downstream diffusion-policy execution of a squat-and-lift task across payload conditions. Website: https://bb0928.github.io/forge/.

---

### Top 2: EgoX: Egocentric Cross-Embodiment Manipulation with Embodiment Dreaming
- **Priority Score**: `95 pts` | **Published**: `2026-11-12`
- **Focus Tracks**: `#humanoid`
- **Key Authors**: Yaru Niu, Binghong Chen, Changwei Yao et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2611.16728v1) | [PDF Fulltext](http://arxiv.org/pdf/2611.16728v1)

**Executive Abstract**:
> Generalist manipulation policies can benefit from the complementary experience of humans, real robots, and simulated agents. However, differences in morphology, sensing, and control interfaces make it difficult to learn effectively from their combined demonstrations. We introduce EgoX, an egocentric cross-embodiment learning framework that organizes heterogeneous demonstrations through semantically corresponding observation and action modalities. EgoX pretrains a Modularized Cross-Embodiment Transformer with Embodiment Dreaming (MXT+) on this mixture and fine-tunes it on target-embodiment demonstrations. Within each embodiment, MXT+ assigns a dedicated tokenizer to each observation modality and a dedicated expert to each action modality, with a Transformer trunk shared across embodiments. A training-only embodiment-dreaming objective predicts latent representations of future visual and proprioceptive states, encouraging the shared trunk to model each embodiment's dynamics. Across 13 task-embodiment pairs spanning five tasks and six robot embodiments, including five physical robots and one simulated humanoid, cross-embodiment pretraining raises MXT+'s average normalized task progress from 0.63 to 0.80 over training from scratch. The gains are particularly pronounced under out-of-distribution conditions, where average task progress increases from 0.53 to 0.77. Ablations demonstrate the benefits of broader pretraining mixtures, modular interfaces, and embodiment dreaming, with dreaming producing more similar latent geometry across embodiments. Project page: egox-dream.github.io.

---

### Top 3: UAV-Flow++: A Unified Suite for Benchmarking and Learning Language-Guided UAV Flight
- **Priority Score**: `90 pts` | **Published**: `2026-11-12`
- **Focus Tracks**: `#vla`
- **Key Authors**: Donglin Yang, Xiangyu Wang, Yantong Zhong et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2611.17163v1) | [PDF Fulltext](http://arxiv.org/pdf/2611.17163v1)

**Executive Abstract**:
> Language-guided UAV navigation has largely focused on long-horizon route planning, leaving short-range, object-relative flight maneuvers underexplored. To address this gap, we formulate Flying-on-a-Word (Flow), a task requiring a UAV to convert concise natural-language instruction, egocentric visual observation, and current state dynamics into continuous flight actions. Flow encompasses both primitive motion commands and complex object-interactive behaviors, assessing motion intent comprehension and spatial context grounding. To enable policy learning and closed-loop evaluation, we introduce UAV-Flow, a comprehensive dataset comprising 30,692 expert-piloted real-world trajectories across eight distinct motion categories, alongside 10,109 simulation trajectories in the UAV-Flow-Sim environment equipped with task-specific completion criteria. Furthermore, we develop FlowVLA, which undergoes imitation pretraining on mixed real-sim demonstrations and online post-training via Tail-Aware GRPO (TGRPO). By leveraging group reward distributions, TGRPO effectively reinforces high-reward action sequences. Evaluated on 273 held-out UAV-Flow-Sim episodes, pretrained FlowVLA achieves a mean success rate of 75.58%, outperforming the strongest baseline by 6.72 percentage points, which TGRPO post-training further elevates to 93.16% with superior sample efficiency. Physical UAV experiments demonstrate robust execution of object-relative commands in both indoor and outdoor real-world scenes. Together, Flow establishes a novel benchmark and learning framework for language-conditioned flight maneuvers.

---

### Top 4: Inner Product Regularization for Imitation Learning
- **Priority Score**: `85 pts` | **Published**: `2026-11-12`
- **Focus Tracks**: `#diffusion policy`
- **Key Authors**: Benjamin A. Christie, Tianyu Qiu, Amy H. Choi et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2611.17159v1) | [PDF Fulltext](http://arxiv.org/pdf/2611.17159v1)

**Executive Abstract**:
> Robots that learn from demonstrations should extrapolate their policy despite state perturbations such as sensor noise, scene variation, and compounding errors. One approach to this robustness is regularization. Prior regularizers consider each state on its own and limit how sensitive the policy is to any perturbation at that state. By contrast, we explore how the policy's output shifts when given the same perturbation at different states. Our insight is that, locally, the robot should respond to state perturbations in a consistent manner: e.g., if changing an irrelevant object position does not impact the policy at one state, that same change should not shift the policy output at a nearby state. Applying this insight, we develop inner product regularization (InneR). We show that the inner product on action space induces an inner product on state space through the policy Jacobian (the Fisher information for stochastic policies), and that the null space of this inner product governs which state perturbations have a first-order effect on the policy. By clustering states whose inner products are aligned, averaging the inner products within each cluster, and minimizing the smallest eigenvalues of that average, InneR shapes the learned policy so that nearby states share a common null space. InneR enforces consistent responses to perturbations without limiting policy expressiveness, and can be appended to existing imitation learning pipelines for deterministic or stochastic policies. In simulated experiments, InneR makes learned policies more robust to irrelevant state dimensions and shifts between training and test distributions, whereas norm penalties often perform worse than behavior cloning. On a real robot arm performing three manipulation tasks, InneR raises the average success rate of a diffusion policy from 18% to 57% without additional data.

---

### Top 5: AgriSense: Vision-Language Decision Support and Robotic Intervention in a Virtual Greenhouse Copy title
- **Priority Score**: `85 pts` | **Published**: `2026-11-12`
- **Focus Tracks**: `#quadruped`
- **Key Authors**: Lyes Saad Saoud, Oualid Doukhi, Reza Ghorbani et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2611.16752v1) | [PDF Fulltext](http://arxiv.org/pdf/2611.16752v1)

**Executive Abstract**:
> Autonomous greenhouse management increasingly requires robotic systems that integrate perception, navigation, environmental regulation, and plant-level intervention. This paper presents AgriSense, a framework combining an Isaac Sim virtual greenhouse, a quadruped mobile manipulator, RGB and LiDAR-inertial sensing, environmental control, and supervised vision-language decision support. Frozen DINOv2 and BERT encoders, together with structured environmental inputs, support joint prediction of twelve environmental references, a target zone, and an intervention flag. Checkpoint replay reproduces 41/43 zone decisions. Across five seeds on a source-grouped test set, the full, image-removed, and language-removed configurations each achieve 43/44 correct zone decisions, providing no evidence of incremental multimodal zone-accuracy improvement. The full model achieves mean absolute errors of 0.249 degrees C for temperature, 2.030 percentage points for humidity, and 0.997 percentage points for soil moisture. Sensor-only inputs match full-model zone accuracy, while language-only inputs achieve 68.64%. External real-image benchmarks reveal distribution-shift limitations. Five offline Point-LIO routes yield rigidly aligned trajectory errors of 5.22-17.32 mm. Of 40 virtual-arm targets, 32 satisfy geometric acceptance criteria and eight are rejected at boundaries. Six long-horizon climate cases and fault protocols characterize integration limits. Navigation and integrated treatment rely on simulator-state inputs; physical greenhouse performance and agronomic treatment efficacy remain unvalidated. The contribution is an evaluated decision-support and robotic-intervention framework for a virtual greenhouse.

---

