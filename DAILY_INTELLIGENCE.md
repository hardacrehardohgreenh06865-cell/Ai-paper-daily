# 🤖 Embodied AI & Robotics Frontier Briefing (2026-10-18)

> *Automated Intelligence Briefing generated via custom ETL scoring pipeline. Prioritizes foundation models, manipulation, locomotion, and physical AI systems.*

---

### Top 1: Dexterity from Supervised Play
- **Priority Score**: `150 pts` | **Published**: `2026-10-15`
- **Focus Tracks**: `#world model` `#reinforcement learning` `#dexterous manipulation`
- **Key Authors**: Botao He, Yiming Dou, Yiannis Aloimonos et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2610.22340v1) | [PDF Fulltext](http://arxiv.org/pdf/2610.22340v1)

**Executive Abstract**:
> How can robots autonomously collect the contact-rich experience needed to learn dexterous manipulation? We present DSP: Dexterity from supervised play, a framework in which a robot learns a play policy from minutes of human play through behavior cloning, then deploys it autonomously to collect hours of interaction data to train a world model. During inference, the same play policy then guides model-predictive control (MPC) by proposing candidate action sequences for evaluation under the learned world model. To accelerate inference, we also introduce a method for distilling a closed-loop, goal-conditioned policy through self-play within the learned world model. We evaluate this framework on underactuated pushing and any-to-any in-hand pose reorientation with a multifingered hand, in simulation and real world. In real world experiment, our method outperforms hindsight behavior cloning by 69.6% in success rate and achieves comparable success to reinforcement learning with 490 times less interaction data. These results demonstrate that supervised play can autonomously collect interaction data, guide model-based planning, and enable policy learning without any task-specific demonstrations or sim-to-real transfer.

---

### Top 2: REKI: Registering Knowledge in VLAs
- **Priority Score**: `135 pts` | **Published**: `2026-10-15`
- **Focus Tracks**: `#vision-language-action` `#vla`
- **Key Authors**: Juliette Marrie, Paul Pacaud, Adrien Ramanana Rahary et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2610.22178v1) | [PDF Fulltext](http://arxiv.org/pdf/2610.22178v1)

**Executive Abstract**:
> We introduce REKI, a 2.4B vision-language-action model (VLA) pretrained exclusively on public data that sets a new Pareto frontier between performance and model size: on LIBERO-Plus, RoboTwin Clean2Rand and RoboCasa365, it is outperformed only by models about twice its size. REKI consists of a vision-language model (VLM) followed by a flow-matching action expert, and is pretrained on a curated mixture of public robot, egocentric human and vision-language data. Additionally, we endow it with a memory that gives the policy access to its recent past at negligible cost: a few register tokens in the action expert summarise the output of the VLM at each frame and persist in the expert's cache. This memory improves success in simulation and on real robots, and makes oscillations between poses about four times rarer. REKI uses a simple model design and training paradigm, and is optimised to be efficient at training and inference. We release the full code across data curation, training, inference and evaluation, deployment, and all pretrained and finetuned model weights: https://github.com/kyutai-labs/reki.

---

### Top 3: FastVLA: Task-Conditioned and Temporally Adaptive Visual Token Compression for Efficient Vision-Language-Action Models
- **Priority Score**: `135 pts` | **Published**: `2026-10-15`
- **Focus Tracks**: `#vision-language-action` `#vla`
- **Key Authors**: Jiuyi Xu, Chengyuan Qian, Zhengzhong Tu et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2610.22146v1) | [PDF Fulltext](http://arxiv.org/pdf/2610.22146v1)

**Executive Abstract**:
> Vision-Language-Action (VLA) models present a promising paradigm for general-purpose robot manipulation, but closed-loop deployment is often limited by inference efficiency: at each timestep, high-resolution, often multi-view images are encoded into hundreds of visual tokens that dominate transformer computation and latency. Token compression via attention is a natural solution but is challenging for VLA control because (1) decision-critical tokens are determined by the task, not generic visual saliency, and (2) the token budget varies substantially across steps, so static metrics and budgets waste computation or discard control-critical tokens. We introduce FastVLA, a training-free, task-aware, and temporally adaptive visual token compression framework. At each step, FastVLA scores token importance via task-to-vision attention and adaptively sets the compression rate from the importance-distribution uniformity, measured by an inverse-Simpson metric with online sliding-window calibration. We evaluate FastVLA on OpenVLA, OpenVLA-OFT, and CogACT across LIBERO and SIMPLER, and on a physical Franka Research 3 robot. In simulation, it reduces LLM-backbone FLOPs by 35-59\% and action latency by 9-32\% (a 1.09$\times$-1.46$\times$ speedup) while maintaining task success, achieving a comparable or better efficiency-performance trade-off than existing plug-and-play token compression/pruning/reuse baselines. On the real robot, it cuts end-to-end latency by 20\% (1.25$\times$ speedup) at comparable success. Code is available at https://github.com/jiuyixu25/FastVLA.

---

### Top 4: Spark-0: Scaling Spatially Aligned Tactile Pretraining for Robot Dexterous Manipulation
- **Priority Score**: `125 pts` | **Published**: `2026-10-15`
- **Focus Tracks**: `#humanoid` `#dexterous manipulation`
- **Key Authors**: Tianxing Chen, Wenwei Lin, Chuqiao Lyu et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2610.22342v1) | [PDF Fulltext](http://arxiv.org/pdf/2610.22342v1)

**Executive Abstract**:
> Generalist robot policies benefit from large-scale visual pretraining but often struggle with contact-rich dexterous manipulation, where force, compliance, and incipient slip are hard to observe from images. We present Spark-0, a spatially aligned vision-tactile-language-action (VTLA) model that uses touch in two complementary ways. During pretraining, image-space contact maps derived from tactile gloves, together with features from a frozen 3D geometry teacher, supervise the visual tokens; these objectives are removed at inference. In parallel, a tactile pathway encodes regional force histories and 3D taxel states to condition the action expert. A single checkpoint therefore supports both vision-only and tactile-conditioned deployment. To scale this supervision, we build HumanTouch, a 1,000-hour dataset of full-hand tactile human manipulation, and pretrain Spark-0 on it together with egocentric video, robot data, and simulation. We also release SparkArena, which pairs vision-only simulated tasks with tactile-conditioned real-robot tasks on one dexterous embodiment. Spark-0 achieves the highest mean success rate on both SparkArena tracks and ranks first on all eight aggregate metrics of the Ego Humanoid Manipulation Benchmark. Compared with vision-only pretraining on the same data and compute with touch discarded, retaining the touch of 1,000 hours of HumanTouch raises vision-only success on Ego Humanoid from 52.5% to 71.7%, and success on SparkArena-Real, where touch is also used at deployment, from 44.0% to 52.0%, indicating that touch serves not only as a policy input but also as scalable supervision for dexterous visuomotor pretraining. The Website is available at: https://xsparkai.com/Spark-0.

---

### Top 5: Whole-Body Dexterity
- **Priority Score**: `125 pts` | **Published**: `2026-10-15`
- **Focus Tracks**: `#humanoid` `#dexterous manipulation`
- **Key Authors**: Conor Mc Gartoll, An Dang, Pranay Thangeda et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2610.22184v1) | [PDF Fulltext](http://arxiv.org/pdf/2610.22184v1)

**Executive Abstract**:
> Current humanoid dexterous manipulation remains largely confined to end-effectors and simple grasps, falling short of humans' ability to engage the entire body by bracing and sliding bulky objects against the arms and torso. We introduce Whole-Body Dexterity (WBD), a general framework that uses the robot's body and appendages as contact surfaces to grasp and manipulate objects. Our sim-to-real pipeline first generates a dataset of feasible whole-body grasps, then trains reinforcement-learning experts on a general any-to-any repositioning objective by sampling initial and goal grasps from the dataset, and distills these experts into a single policy that uses proprioception and object geometry. We show that the distilled policy transfers zero-shot to a real Unitree G1, where it repositions a basketball and a cardboard box to regions around the torso and completes a long-horizon task that stows a box under one arm, carries it from a shelf to a table, and places it. The controller operates interactively, steered by coarse motion references from a human teleoperator. Across real-world whole-body manipulation tasks, the distilled controller completes 90% of trials, compared with 18% for direct retargeting and 4% for a generalist whole-body controller.

---

