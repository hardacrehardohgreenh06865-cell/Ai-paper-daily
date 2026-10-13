# 🤖 Embodied AI & Robotics Frontier Briefing (2026-10-13)

> *Automated Intelligence Briefing generated via custom ETL scoring pipeline. Prioritizes foundation models, manipulation, locomotion, and physical AI systems.*

---

### Top 1: RARA: Robust Policy Fine-Tuning through Retrieval-Anchored Representation Alignment for Robotic Manipulation
- **Priority Score**: `170 pts` | **Published**: `2026-10-09`
- **Focus Tracks**: `#diffusion policy` `#vision-language-action` `#vla`
- **Key Authors**: Xuhui Kang, Sung-Wook Lee, Yan Zhuang et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2610.13578v1) | [PDF Fulltext](http://arxiv.org/pdf/2610.13578v1)

**Executive Abstract**:
> Pre-trained robot policies, such as Vision-Language-Action (VLA) models, provide a strong foundation for generalist robotic manipulation, but adapting them to new tasks with only a few demonstrations remains challenging. Directly fine-tuning a pre-trained policy often achieves strong in-distribution performance, yet it can distort the representations learned during pre-training and weaken the model's generalization ability under out-of-distribution shifts. We propose Retrieval-Anchored Representation Alignment (RARA), a two-stage adaptation method, to address this issue. First, RARA retrieves representation features from pretraining with similar task intent and motion, and aligns the policy's representations of the target demonstrations with the pre-trained representations of the retrieved demonstrations. Second, RARA fine-tunes the policy on the target demonstrations while limiting how much its representations of the retrieved demonstrations change during fine-tuning. By reducing the representation mismatch before action learning and preserving pre-trained knowledge during adaptation, RARA limits unnecessary representation drift during fine-tuning. Experiments with Diffusion Policy and GR00T on 13 tasks in RoboTwin, RoboCasa, and on a real robot show that RARA improves the average success of fine-tuning by 9.5 points in-distribution and 13.6 points out-of-distribution, and outperforms all compared baselines. Project page: https://shua-kang.github.io/RARA_robot/

---

### Top 2: Splat2Act: From Captured Scenes to Personalized VLA Manipulation
- **Priority Score**: `135 pts` | **Published**: `2026-10-09`
- **Focus Tracks**: `#vision-language-action` `#vla`
- **Key Authors**: Xiaomeng Ye, Krishna Jaganathan, Gyubeum Lim et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2610.13945v1) | [PDF Fulltext](http://arxiv.org/pdf/2610.13945v1)

**Executive Abstract**:
> A user who brings a generalist manipulation policy into their home or office wants it to pick up their objects from their shelves, counters, and tables. Yet even a strong generalist like $π_{0.5}$ achieves 0% pickup success in our captured deployment scenes without adaptation, and collecting real demonstrations in every user's environment is prohibitively expensive. We present Splat2Act, an automated real-to-sim-to-real pipeline that personalizes a pretrained vision-language-action (VLA) policy to a specific scene and object set using only a handheld phone scan and images of the user's objects. Unlike prior real-to-sim work that reconstructs individual tabletops, Splat2Act operates on building-scale indoor environments: it builds a photorealistic digital twin with 3D Gaussian Splatting and collision geometry, automatically discovers tabletop and non-tabletop receptacles, constructs feasible pickup tasks, and generates successful demonstrations with a privileged simulation oracle, with only scene and object capture required from a human. Applied to 101 scanned campus environments with a median navigable area of 104.87 m$^2$ and 7 receptacles, the pipeline yields 852 receptacles and over 68,000 pickup demonstrations. We fine-tune $π_{0.5}$ in two stages: Stage 1 adapts to hundreds of public object assets, drawn either from the deployment scene alone or from all 101 scenes; Stage 2 personalizes to the user's own objects on the deployment scene's receptacles. Our strongest personalized policy reaches 62.5% aggregate pickup success in the target scene. Deployed on a real Stretch 3, the same policy achieves 63.9% success on a 12-task subset, closely tracking its 66.7% simulated success on those tasks. These results suggest that automated real-to-sim-to-real training can personalize VLA manipulation policies using only simulation-oracle data.

---

### Top 3: Noise Space Learning for VLA Adaptation
- **Priority Score**: `135 pts` | **Published**: `2026-10-09`
- **Focus Tracks**: `#vision-language-action` `#vla`
- **Key Authors**: Junjie Lu, Chuheng Zhang, Yucen Wang et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2610.13943v1) | [PDF Fulltext](http://arxiv.org/pdf/2610.13943v1)

**Executive Abstract**:
> Pretrained vision-language-action (VLA) models encode broad manipulation priors, yet adapting them to specific tasks requires balancing limited robot interaction, computational resources, and safety constraints. Noise space learning (NSL) adapts flow-matching-based VLAs by learning a context-conditioned distribution over noise while keeping the pretrained VLA fixed. Building on prior noise-steering methods, we formulate NSL as an interface for VLA adaptation that accommodates different learning algorithms and instantiate it with PPO, SAC, and AWR. Theoretically, we provide an information-theoretic analysis of how NSL enables efficient adaptation. Empirically, we study these NSL algorithms on LIBERO, RoboTwin, and four real-robot manipulation tasks under interaction, computation, and execution constraints. Across these settings, we develop a suite of effective NSL variants and derive practical recommendations for choosing among them under different resource and deployment regimes.

---

### Top 4: JitterVLA: A Replay Benchmark for Motion Quality in VLA-Driven Human-Robot Manipulation
- **Priority Score**: `135 pts` | **Published**: `2026-10-09`
- **Focus Tracks**: `#vision-language-action` `#vla`
- **Key Authors**: Faith Ogunwoye, Didar Seyidov, Konstantin Gubernatorov et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2610.13628v1) | [PDF Fulltext](http://arxiv.org/pdf/2610.13628v1)

**Executive Abstract**:
> Vision-language-action (VLA) policies issue sparse targets whose arrival at the robot controller is delayed and irregular, so a reasonable predicted action can still produce abrupt motion near people. Remedies are evaluated on different streams, delays and metrics. JitterVLA replays identical commands and arrival traces through alternative controllers, isolating the controller's effect. We apply it to synthetic reaches, hand trajectories from 20 people, three open VLA pipelines (838 episodes) and a physical UR3. Interpolation lowered modeled p99 jerk for every source, by 83% (615 to 106 m/s^3) on human motion with 200 ms delay, at a 2.0 cm tracking cost, and the effect replicated on 598 new episodes; jerk-limited generation lowered jerk further at a larger cost. Entropy-discontinuity associations had opposite, replicated signs in two pipelines, and entropy gating helped in one but not the other. On the UR3, interpolation lowered accelerometer-derived jerk by 3.0-14.0% in all six exploratory pairs, while a position-derived metric did not resolve the contrast. JitterVLA supports screening before human-centred studies; code and data will be released.

---

### Top 5: Dream to Remember: Continual Steering of Generalist Robot Policies with World Models
- **Priority Score**: `120 pts` | **Published**: `2026-10-09`
- **Focus Tracks**: `#world model` `#reinforcement learning`
- **Key Authors**: Bahey Tharwat, Iman Nematollahi, Marvin Alles et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2610.13816v1) | [PDF Fulltext](http://arxiv.org/pdf/2610.13816v1)

**Executive Abstract**:
> Generalist robot policies are trained with imitation learning and are bounded by the quality and coverage of their demonstrations. Reinforcement learning can improve and extend them, either by fine-tuning the policy weights or by training a small module to steer the input noise of a frozen generative policy. When tasks arrive sequentially, both approaches suffer from catastrophic forgetting. Fine-tuning on a task degrades prior tasks, and steering only shifts forgetting to the shared steering module. We propose Dream to Remember (D2R), which continually steers a frozen generalist policy toward new tasks, while retaining its earlier skills. As the steering module learns a new task, a frozen pretrained world model rehearses prior tasks through imagined rollouts, anchoring the module to its earlier behavior without a replay buffer or new data. When the world model is faithful enough, D2R learns the new task entirely in imagination. Otherwise, it learns the task in the environment while using the world model only to rehearse prior tasks. On CALVIN, D2R improves eight tasks in sequence entirely in imagination, raising average success from 63.7% to 74.8%, while LoRA fine-tuning on the same sequence drops it to 11.7%. With a frozen off-the-shelf generalist policy and world model, $π_0$ and A2World, D2R learns unseen LIBERO-90 tasks in the environment while keeping $π_0$'s performance on the LIBERO suites it was fine-tuned on, even though the world model is not accurate enough for policy optimization. Finally, on a real Franka robot, D2R improves three tasks in sequence entirely in imagination while retaining the earlier improvements.

---

