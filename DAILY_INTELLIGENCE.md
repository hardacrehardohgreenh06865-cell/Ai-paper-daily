# 🤖 Embodied AI & Robotics Frontier Briefing (2026-11-09)

> *Automated Intelligence Briefing generated via custom ETL scoring pipeline. Prioritizes foundation models, manipulation, locomotion, and physical AI systems.*

---

### Top 1: ForPC: Force-Aware Whole-Body Control for Precise Humanoid Cart Pushing
- **Priority Score**: `170 pts` | **Published**: `2026-11-05`
- **Focus Tracks**: `#humanoid` `#reinforcement learning` `#locomotion` `#actuator`
- **Key Authors**: ZhenYu Zou, Xing Liu, ShiChuang Wang et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2611.08664v1) | [PDF Fulltext](http://arxiv.org/pdf/2611.08664v1)

**Executive Abstract**:
> Humanoid robots are expected to take over strenuous material handling in manufacturing, logistics, and healthcare, where operating existing wheeled carts would let them move heavy loads without modifying the workplace. However, humanoid cart pushing remains challenging because the bimanual grasp closes a force-coupled loop in which the contact wrenches that drive the cart also disturb the robot's balance, and payload changes alter the coupled dynamics. We propose ForPC, a force-aware whole-body control framework that regulates cart velocity through two-stage reinforcement learning. A locomotion prior is first trained under varied hand loads and upper-body postures to provide balance support. A force latent and a state latent are then inferred from onboard observations, without external force sensors, and fed to a residual policy that coordinates bounded arm, waist, and leg adjustments with base-velocity commands. Multi-objective rewards penalize bimanual internal opposition, grasp slip, and actuator saturation, encouraging the policy to apply contact force on demand without human demonstrations. Sim-to-sim experiments show that ForPC reduces cart-velocity RMSE by up to 68.2% relative to a locomotion-only baseline (Loco-only) and cross-track RMSE by up to 74.2% on the multi-bend route. Trained solely in simulation, the policy also transfers to a physical Unitree G1 without real-world training or fine-tuning and, with no payload-specific adjustment, pushes a cart carrying up to 30 kg at 0.5 m/s. These results suggest that humanoid robots could eventually replace humans for efficient material handling in daily life.

---

### Top 2: STRIDE: Learning Humanoid Locomotion in Minutes with Acceleration-Based Rewards
- **Priority Score**: `150 pts` | **Published**: `2026-11-06`
- **Focus Tracks**: `#humanoid` `#reinforcement learning` `#locomotion`
- **Key Authors**: Nico Bohlinger, Jan Peters
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2611.08857v1) | [PDF Fulltext](http://arxiv.org/pdf/2611.08857v1)

**Executive Abstract**:
> Learning locomotion directly on a humanoid robot is a promising direction to avoid the sim-to-real gap. However, locomotion rewards in Reinforcement Learning (RL) typically track the base velocity, which cannot be measured onboard without an external motion capture system or well-calibrated state estimator. This is why we introduce \method{}, which learns humanoid locomotion from minutes of samples with a reward that only requires the onboard Inertial Measurement Unit (IMU). Instead of tracking the base velocity, STRIDE rewards the robot for following a commanded acceleration profile. To learn efficiently from this reward, we use the off-policy RL algorithm XQC and combine a high gain setting for the joint position controllers with left-right symmetry augmentation. In simulation, STRIDE learns to walk on the Unitree G1 and Booster T1 humanoids within 14 minutes of samples. Compared to learning without these two components, it reduces the falls during training by 81%, while without them the robot learns only in over an hour.

---

### Top 3: PRISM: Primitive Routing via In-context Skill Mixing for Retentive VLA Adaptation
- **Priority Score**: `135 pts` | **Published**: `2026-11-06`
- **Focus Tracks**: `#vision-language-action` `#vla`
- **Key Authors**: Jiachen Tao, Gengyu Zhang, Haoxuan Wang et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2611.08917v1) | [PDF Fulltext](http://arxiv.org/pdf/2611.08917v1)

**Executive Abstract**:
> Vision-Language-Action (VLA) models promise a single language-conditioned policy adaptable to many manipulation behaviors, yet deployment additionally requires skill retention and long-horizon composition: a policy must retain previously acquired skills and reuse them inside composite tasks whose behavior changes across phases. The standard recipe absorbs every new task into one shared update, which provides neither a parameter-level locus for reusable skills nor a mechanism for invoking each skill along the trajectory. We observe that this missing structure is latent rather than absent: per-skill low-rank updates of a pretrained VLA occupy a robustly distinguishable, low-dimensional subspace, and a single composite-task LoRA concentrates roughly half of its Frobenius energy in this subspace, against a near-zero matched random-rotation control. Building on this geometry, we introduce PRISM, which represents reusable skills as parameter-level primitives: each skill family is stored as a dedicated low-rank action-expert adapter in a primitive bank, primitives are augmented with skill-specific low-rank residuals and composed at inference by a per-chunk VLM-conditioned router that reads the prefix representation to track task progress, and the router is supervised by per-chunk labels from a deterministic, task-conditioned, action-derived oracle. During composite training, the vision encoder, the language LoRA, the skill residuals, the router, and the shared action projections and time MLP are updated; every primitive is held frozen, so the base per-skill action-expert adapters are preserved by construction. On RoboCasa365, PRISM achieves 56.43% atomic-skill success and reaches 20.00% on long-horizon composite tasks, while a standard $π_{0.5}$-LoRA two-stage fine-tune reaches 17.86% atomic and 17.50% composite success. We additionally validate PRISM on an AgileX PIPER real-robot setup.

---

### Top 4: Localizing and Editing the Goal Representation of a Vision-Language-Action Model
- **Priority Score**: `135 pts` | **Published**: `2026-11-06`
- **Focus Tracks**: `#vision-language-action` `#vla`
- **Key Authors**: Sudhanshu Srivastava, Faisal Aqlan
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2611.08895v1) | [PDF Fulltext](http://arxiv.org/pdf/2611.08895v1)

**Executive Abstract**:
> Operators can state safety constraints for robots as prohibitions such as "do not put the bowl on the stove". We study whether OpenVLA follows such prohibitions and where it represents the goal it executes. The 10 tasks of LIBEROGoal share one scene, so we can label the goal that each rollout executes. We combine closed-loop rollouts with activation patching, linear probes, activation steering and runtime monitors. On LIBERO-Goal, negation had no detectable effect on which task OpenVLA executed. The model executed the forbidden task in 79% of negated rollouts and completed 78% of plain tasks. A goal probe gives similar read-outs under "not X" and "X". Activation patching shows that the first action depends mostly on the instruction tokens before layer 12 and on the last prompt token from layer 16 onward. A fixed steering vector at the instruction tokens at layer 8 redirected 12 of 18 rollouts. Fixed vectors and prefill patches at layers 12 to 20 redirected none of 158. From layer 16, only patches at every decoded action token redirected the robot (15 of 18 rollouts at layer 24). When the instruction changes during a rollout, the layer-32 goal read-out detects non-compliance better than failure detectors, and an external probe on image and instruction features performs comparably. These results support enforcing prohibitions outside the instruction and monitoring goal read-outs against the specification. Goal edits in OpenVLA should act before layer 12 or patch every action token.

---

### Top 5: ActPrune: Action-Grounded Visual Token Pruning for Efficient Vision-Language-Action Models
- **Priority Score**: `135 pts` | **Published**: `2026-11-06`
- **Focus Tracks**: `#vision-language-action` `#vla`
- **Key Authors**: Sungwon Moon, Minji Kim, Hyemin Boo et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2611.08827v1) | [PDF Fulltext](http://arxiv.org/pdf/2611.08827v1)

**Executive Abstract**:
> Vision-language-action (VLA) models perform versatile manipulation tasks from language instructions, but their inference cost limits how fast a robot can respond in closed-loop control. Visual token pruning reduces this cost; however, prior methods estimate token redundancy from encoded visual embeddings or attention, only after the visual encoder has processed the entire observation. We propose \ours, a training-free token pruning method that moves the pruning decision ahead of the vision encoder by grounding it in a geometric prior derived from the robot's own action. The action chunk predicted at the previous control step is already available before the current observation is encoded, and it specifies the end-effector and camera motion between consecutive observations. The same action affects the two standard camera views asymmetrically: in the fixed third-person view, \ours retains patches along the projected end-effector trajectory together with semantic anchors, while in the wrist view, it prunes patches that remain unchanged after compensating for the action-induced camera motion. Extensive experiments on two simulation environments (LIBERO and VLABench) and four real-robot tasks demonstrate that \ours achieves up to 1.61 $\times$ speedup and 59.5\% FLOPs reduction with negligible degradation in success rates.

---

