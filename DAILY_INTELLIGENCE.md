# 🤖 Embodied AI & Robotics Frontier Briefing (2026-09-18)

> *Automated Intelligence Briefing generated via custom ETL scoring pipeline. Prioritizes foundation models, manipulation, locomotion, and physical AI systems.*

---

### Top 1: Compliance for Free: Learning Identifiable Impedance via Bilateral Teleoperation
- **Priority Score**: `155 pts` | **Published**: `2026-09-17`
- **Focus Tracks**: `#vision-language-action` `#vla` `#teleoperation`
- **Key Authors**: Harsha Guda, Adrià Colomé, Carme Torras
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2609.19976v1) | [PDF Fulltext](http://arxiv.org/pdf/2609.19976v1)

**Executive Abstract**:
> Vision-language-action models tell a robot where to move, but not how hard to push. Contact-rich tasks depend on that second quantity, compliance, yet no widely used demonstration interface records it. The obstacle is identifiability as realized pose and measured force cannot separate the operator's intended equilibrium from their stiffness, so VR controllers, SpaceMouse and handheld grippers cannot supply compliance supervision even in principle. Prior compliance-output policies work around this with hand-specified task structure, privileged simulation contact state, or dedicated force and tactile hardware. Four-channel bilateral teleoperation removes the ambiguity directly by using the leader arm as a separate measurement of the intended equilibrium, making per-axis stiffness identifiable by regression using only the joint-torque sensing already on the manipulator. This yields per-timestep, direction-dependent compliance labels at zero annotation cost, which we use to fine-tune a VLA to emit stiffness alongside pose. On a Franka Research 3 wiping task, ours is the only policy of five whose contact force changes when the instruction asks for a firm wipe rather than a normal one (6.4N (normal) to 9.1N (firm) RMS, Cohen's d = 0.89, p = 0.023

---

### Top 2: Co-VLA: Consensus-based Federated Training for Vision-Language-Action Models
- **Priority Score**: `135 pts` | **Published**: `2026-09-17`
- **Focus Tracks**: `#vision-language-action` `#vla`
- **Key Authors**: Haolong Li, Guner Dilsad Er, Michael Muehlebach et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2609.19923v1) | [PDF Fulltext](http://arxiv.org/pdf/2609.19923v1)

**Executive Abstract**:
> Vision-language-action models (VLAs) have emerged as a promising paradigm for general-purpose robot learning, with performance improving as models and datasets scale. Scaling robot data collection, however, remains challenging because data are naturally distributed across robots, tasks, and locations, making centralization costly or impractical. Federated learning offers a way to train on decentralized robot data, but applying it to VLAs requires accounting for heterogeneous robot client data distributions. We present Co-VLA, which applies consensus optimization using the Alternating Direction Method of Multipliers~(ADMM) to federated VLA training. We show that the same algorithm supports both full-model training and parameter-efficient fine-tuning with both fixed-rank and rank-adaptive adapters. The name Co-VLA reflects both consensus and collaboration: clients with different local robot datasets collaboratively train a shared model without sharing their data. Our experiments demonstrate that Co-VLA achieves performance comparable to centralized training in both full-model training and parameter-efficient fine-tuning settings.

---

### Top 3: AnyViewDex: View-Invariant Dexterous Manipulation from RGB Observations
- **Priority Score**: `110 pts` | **Published**: `2026-09-17`
- **Focus Tracks**: `#reinforcement learning` `#dexterous manipulation`
- **Key Authors**: Soham Patil, Om Sanjay Gunjal, Sourabh Bhosale et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2609.20107v1) | [PDF Fulltext](http://arxiv.org/pdf/2609.20107v1)

**Executive Abstract**:
> Visuomotor policies for multi-fingered dexterous manipulation are highly sensitive to camera viewpoint shifts. To achieve view invariance, recent methods increasingly rely on explicit 3D modalities like RGB-D or point clouds, which can introduce hardware dependencies, calibration requirements, and vulnerability to sensor noise during real-world deployment. In this work, we show that view-invariant control can be achieved without explicit test-time 3D sensing by encoding geometric knowledge into the visual representation during simulation. We present AnyViewDex, an asymmetric training pipeline that combines multi-view contrastive alignment with privileged 3D geometric supervision. By regressing absolute 3D object coordinates during simulated training, this auxiliary objective provides a geometric grounding signal that mitigates the spatial collapse of the globally pooled contrastive embedding. At deployment, the policy operates zero-shot using only uncalibrated monocular RGB and proprioception. We validate this approach across both reinforcement learning and student-teacher distillation. In hardware evaluation on an xArm7 with a 16-DoF LEAP Hand, AnyViewDex reaches 76.7% grasping success across eight unseen objects and six uncalibrated viewpoints (480 trials; 2,400 across all ablation conditions), indicating that geometrically grounded monocular policies transfer zero-shot without test-time depth. Project Page: https://anyviewdex.github.io/

---

### Top 4: DR-MPC: Fast and Feasible Dynamics-Relaxed Model-Predictive Control for Legged Locomotion
- **Priority Score**: `110 pts` | **Published**: `2026-09-17`
- **Focus Tracks**: `#quadruped` `#locomotion`
- **Key Authors**: Run Wang, Alapati Tuerxun, Shuo Liu et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2609.20035v1) | [PDF Fulltext](http://arxiv.org/pdf/2609.20035v1)

**Executive Abstract**:
> This paper presents dynamics-relaxed model predictive control (DR-MPC), a novel MPC formulation for legged locomotion, and a tailored interior-point method (IPM) solver. The formulation combines online optimization feasibility by construction with a contact-aware input parameterization. DR-MPC moves the dynamics equality and affine input constraints into quadratic penalties and retains only nonempty box constraints. The resulting box-constrained quadratic program (QP) has a block-arrow Hessian that enables the state and affine-output directions to be eliminated through a Schur complement. The solver factors only the reduced control system after swing-force elimination and contact-aligned move blocking. For the evaluated implementations using the same DR-MPC formulation, our method achieves median end-to-end MPC speedups of $16.0\times$ over HPIPM and $4.4\times$ over OSQP, with comparable locomotion performance in simulation. DR-MPC achieves a median onboard MPC end-to-end time of $4.4$ ms and is validated on a Unitree Go1 quadruped. Open-source code will be made available after publication.

---

### Top 5: Astronex-World 1.0: Real-Time Interactive World Model Foundation
- **Priority Score**: `90 pts` | **Published**: `2026-09-17`
- **Focus Tracks**: `#world model`
- **Key Authors**: Xin Zhou, Cong Miao
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2609.20034v1) | [PDF Fulltext](http://arxiv.org/pdf/2609.20034v1)

**Executive Abstract**:
> We present Astronex-World 1.0, an open controllable video world-model foundation. Given a text prompt (text-to-video) or an initial observation (image-to-video), the model predicts future visual states under frame-aligned camera trajectories, continuous actions, and an embodiment identifier, and accepts text events inserted at a specified position of a rollout. The family provides a bidirectional model for full-context generation and a causal model with block-causal attention and cross-block KV caching for persistent generation, both built on the Wan2.2-TI2V-5B prior. PRoPE injects camera intrinsics and extrinsics, while a 64-dimensional action stream modulates every Transformer layer. A five-stage training path develops bidirectional camera and action control, converts the backbone to block-causal generation, distills a few-step student, restores mixed-domain dynamics, and applies asymmetric DMD/DMD2 distribution matching. The causal model generates 832x480 video at 24 fps. All five training stages run on two NVIDIA L20 48 GB GPUs, and the causal model streams in real time on one. It scores 73.5 on WBench Navi and 70.0 on WBench Full. On Full, this 5B model is above the 13.6B LongCat-Video and the 14B Helios, within one point of the 22B LTX-2.3, and above YUME 1.5, which is post-trained from the same 5B prior on NVIDIA A100 GPUs. The reserved action input and output interfaces allow post-training for embodied intelligence and autonomous driving.

---

