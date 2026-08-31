# 🤖 Embodied AI & Robotics Frontier Briefing (2026-08-31)

> *Automated Intelligence Briefing generated via custom ETL scoring pipeline. Prioritizes foundation models, manipulation, locomotion, and physical AI systems.*

---

### Top 1: Stay Seated: Learning Omnidirectional Humanoid Locomotion on a Passive Mobile Chair with Casters
- **Priority Score**: `140 pts` | **Published**: `2026-08-28`
- **Focus Tracks**: `#humanoid` `#locomotion` `#actuator`
- **Key Authors**: Kango Yanagida, Kazuki Miyazawa, Takato Horii
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2608.28090v1) | [PDF Fulltext](http://arxiv.org/pdf/2608.28090v1)

**Executive Abstract**:
> Humanoid robots with quasi-direct-drive actuators continuously generate joint torque while standing, whereas seated humans delegate weight support to chairs during desk work. As a first step toward seated loco-manipulation, we study omnidirectional seated locomotion on a passive mobile chair, requiring unfixed pelvis-seat contact and intermittent foot-floor propulsion of the robot-chair system. We extend a standard standing velocity-tracking environment with a passive-chair model, seated-state rewards, critic-only chair observations, and task-tailored contact settings. The policy is learned without motion-imitation rewards; its actor uses only proprioception and velocity commands, without contact sensing or chair states. In random-command evaluation, the policies tracked omnidirectional commands through nearly all 20-s rollouts, and the best seated policies could outperform the Standing policy in velocity tracking. Across four training seeds, a $2^3$ full-factorial comparison of symmetry regularization (SY), foot-slip regularization (FS), and command curriculum (CC) showed that FS reduced CoT but increased tracking error and that some FS-only policies converged to stationary local optima. Combining FS with either SY or CC avoided this failure without retuning FS, while SY improved bilateral leg symmetry during longitudinal motion. Direction-resolved analysis showed CoT ordered backward $<$ lateral $\ll$ forward, with planted-leg extension in backward and lateral motion and knee flexion following heel contact in forward motion. The learned policy achieved zero-shot sim-to-real transfer to a Unitree G1 and generated omnidirectional seated locomotion.

---

### Top 2: DeicticVLA: Unifying Instruction Modes Based on Language and Deictic Gestures in a Single VLA
- **Priority Score**: `135 pts` | **Published**: `2026-08-28`
- **Focus Tracks**: `#vision-language-action` `#vla`
- **Key Authors**: Kango Yanagida, Tatsuya Aoki, Yuichiro Yoshikawa et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2608.28108v1) | [PDF Fulltext](http://arxiv.org/pdf/2608.28108v1)

**Executive Abstract**:
> Vision-Language-Action models (VLAs) allow users to specify manipulation tasks in natural language, but distinguishing a target or placement goal among objects of the same category or similar appearance requires detailed expressions that VLAs may not use reliably. We propose DeicticVLA, which canonicalizes Language Instruction (LI), Vision-Language Instruction (VLI), and Visual Instruction (VI) into a text prompt and deictic masks through text-prompt completion and deictic gesture grounding, enabling a single pretrained VLA to handle all three instruction modes. With a shared backbone, demonstrations, and matched training steps, we compare two RGB visual prompting methods, two separate-channel mask prompting methods, and three training strategies in simulation. Under two-stage training, the four prompting methods achieve high in-distribution success but differ in their ability to use deictic masks in unseen layouts. Across methods, training-strategy ablations show that two-stage training improves such use, while retaining second-stage LI data mitigates forgetting without reducing VLI and VI performance. In three real-world tasks, one policy supports all modes. VLI and VI outperform LI under unseen expressions, appearance changes, and novel objects. For unseen categories, both achieve 100% success, compared with 16.7% for jointly trained LI. These results demonstrate the unified three-mode interface and guide DeicticVLA design.

---

### Top 3: Contact-Guided Exploration for Non-Prehensile Locomanipulation with Multi-Critic RL
- **Priority Score**: `115 pts` | **Published**: `2026-08-28`
- **Focus Tracks**: `#quadruped` `#reinforcement learning`
- **Key Authors**: Simone Tolomei, Mayank Mittal, Franco Angelini et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2608.28140v1) | [PDF Fulltext](http://arxiv.org/pdf/2608.28140v1)

**Executive Abstract**:
> Non-prehensile manipulation offers versatile skills for moving and rearranging heavy or bulky objects, particularly when combined with a mobile manipulation platform. However, both model-based and model-free approaches struggle with the complex hybrid dynamics and the sparsity of the contact in these tasks. To address these challenges, we propose a contact-guided exploration strategy implemented within a Multi-Critic Reinforcement Learning (RL) framework. A dedicated exploration critic is trained with a dense contact-seeking reward that guides the end-effector toward meaningful contact points; its influence is progressively decayed to recover a task-optimal policy. We obtain candidate interaction points from a general-purpose grasping algorithm, enabling the exploration mechanism to generalise across various object geometries. We evaluate the approach on multiple tasks, including box pushing, chair transportation, and a dishwasher opening task. Finally, we validate the chair transportation policy through extensive experiments on a quadrupedal mobile manipulator, demonstrating deployable non-prehensile manipulation in the real world.

---

### Top 4: PAMoR: Parameterized Affective Motion Generation in Real Time for Humanoid Robots
- **Priority Score**: `95 pts` | **Published**: `2026-08-28`
- **Focus Tracks**: `#humanoid`
- **Key Authors**: Yan Pan, Lingfan Bao, Tianhu Peng et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2608.28213v1) | [PDF Fulltext](http://arxiv.org/pdf/2608.28213v1)

**Executive Abstract**:
> People read a humanoid robot's motion in social settings not only for the action performed but for the affect conveyed. Motion carrying that affect has so far been generated for human avatars, where style is taken from a reference clip or an emotion word, neither of which can be quantitatively parameterized. We present PAMoR, which turns affect into a measured control parameter: a valence-arousal (V-A) coordinate computed natively on robot kinematics. It is obtained in closed form from postural expansion and movement energy, and these measurements serve directly as generation conditions, with no human annotation. An action prior and two affect priors, trained in a shared latent space, are composed at each denoising step: the action prior fixes what is performed, the affect priors modulate how. Whole-body motion rolls out autoregressively on a 29-DoF Unitree G1 in real time, with action and affect both editable. Generated motion tracks the commanded V-A over its full range while text-to-motion fidelity still matches text-only baselines. In a perceptual study, raters identify the commanded emotion on 0.38 of trials, above both baselines and approaching the 0.44 reported for acted human bodies.

---

### Top 5: LUCID: An Agentic AI Framework on Digital-Twin in the Loop for QoS-Guaranteeing Robotic Control
- **Priority Score**: `50 pts` | **Published**: `2026-08-28`
- **Focus Tracks**: `#general-frontier`
- **Key Authors**: Hyeonsu Lyu, Minwoo Kim, Sehyun Ryu et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2608.28437v1) | [PDF Fulltext](http://arxiv.org/pdf/2608.28437v1)

**Executive Abstract**:
> Cloud robotics relies on the timely uplink of high-volume sensing streams, yet dynamic environments continually shift the feasible combinations of trajectories, active-robot count, and per-robot QoS. Because existing approaches formulate trajectory planning (TP) and radio resource management (RRM) as a single fixed optimization problem, they cannot reconfigure these coupled decisions as conditions evolve, resulting in transient QoS violations. However, evolving operator intents change which quantities-such as the active-robot count and per-robot QoS-are fixed, optimized, or relaxed. Furthermore, the computational cost of evaluating trajectory-dependent wireless conflicts has made it difficult to build large-scale Digital-Twin-in-the-Loop (DITL) testbeds responsive enough for such dynamic orchestration. We present LUCID, an LLM-agent--orchestrated, uplink-aware cloud-robotics pipeline that moves TP--RRM from solving a fixed formulation to dynamically orchestrating optimization problem schemas within a DITL environment. Driven by the operator's high-level intent, LUCID treats the TP--RRM formulation as a bounded template whose variables, objectives, and constraints are dynamically configured, while SimBridge enables repeated ray-tracing evaluation by converting large-scale robotics scenes into wireless-ready DTs. By integrating collision-free path planning with a spectral-radius RRM validator, LUCID identifies wireless bottlenecks and restructures the problem schema on the fly to efficiently find the verified feasible state. Experiments confirm that LUCID robustly adapts to changing intents, active-robot counts, and scenes, while a multimodal surrogate model, FastConfigNet, reduces planning latency.

---

