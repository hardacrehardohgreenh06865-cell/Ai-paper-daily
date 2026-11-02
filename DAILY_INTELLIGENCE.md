# 🤖 Embodied AI & Robotics Frontier Briefing (2026-11-02)

> *Automated Intelligence Briefing generated via custom ETL scoring pipeline. Prioritizes foundation models, manipulation, locomotion, and physical AI systems.*

---

### Top 1: CaPtain: A Pipeline for Post-Training Code-as-Policy Robot Agents
- **Priority Score**: `165 pts` | **Published**: `2026-10-29`
- **Focus Tracks**: `#reinforcement learning` `#vision-language-action` `#vla`
- **Key Authors**: Yijia Fan, Xilin He, Yilei Jiang et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2610.40799v1) | [PDF Fulltext](http://arxiv.org/pdf/2610.40799v1)

**Executive Abstract**:
> Across coding, web, and tool-use tasks, language-model agents are now routinely trained with the same recipe: supervised fine-tuning (SFT) to learn the interface, then multi-turn reinforcement learning (RL) to master it. Code-as-policy (CaP) casts robot manipulation in the same form, as the policy writes code against robot APIs and reads back the results, so the same recipe should apply. Yet existing CaP agents sidestep training: they either prompt closed frontier models or delegate manipulation to pre-trained vision-language-action models (VLAs) and high-level skills, while small open vision-language models (VLMs) fail outright. We present CaPtain, an open post-training pipeline that turns a small open VLM into a capable CaP agent, with no VLA, frontier model, or privileged state at test time. CaPtain trains and deploys the policy inside CaPtain-Harness, which exposes low-level perception, geometry, and guarded-motion primitives across simulation and real hardware. We first align the base model via SFT on synthetic trajectories generated with GPT-6 Astra, then apply multi-turn RL. Multi-turn RL must credit tens of agent requests, whose physical effects often surface turns later, from a single end-of-episode outcome. We therefore introduce a physical critic that reads privileged simulator state, never seen by the policy, and credits each request by how much it changes the predicted chance of success. Starting from Qwen3.5-4B (0% zero-shot), CaPtain-4B reaches 55.4% held-out LIBERO success after SFT and 73.8% after RL. On LIBERO-PRO, it reaches 78.5%, surpassing several frontier-model agents, and its RL gains persist across three perturbation suites (+17.6 to +21.2 points). Without target-domain training, it attains 83.3% on SimplerEnv WidowX, exceeds frontier models on CaP-Bench, and runs on a real robot after simulation-only adaptation. We release all code, data, and model weights.

---

### Top 2: From Teleoperation to Long-Horizon Dexterity: Evaluating Visuomotor Skills and Offline Proxies for Dexterous Manipulation
- **Priority Score**: `145 pts` | **Published**: `2026-10-29`
- **Focus Tracks**: `#dexterous manipulation` `#vision-language-action` `#teleoperation`
- **Key Authors**: Ammar N. Abbas, Aayush Jain, Prashanth Viswanath et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2610.40828v1) | [PDF Fulltext](http://arxiv.org/pdf/2610.40828v1)

**Executive Abstract**:
> Imitation learning policies are intended to make robotic manipulation robust to variations in object pose, appearance, and environment that challenge pre-programmed motion. However, real-world performance remains difficult to predict, as conventional optimization signals such as validation loss show no consistent relationship with robot success. To identify the design choices that govern real-world performance, 281 imitation-learning policies spanning seven policy families were evaluated in approximately 1,700 real-robot trials of RJ45 connector grasping and insertion using a five-fingered robotic hand. Controlled ablations showed that observation and action representations dominated conventional optimizer and sampling choices. For point-cloud policies, region-of-interest cropping, representation in the robot-base frame, and normalization within the point encoder each improved success by 70-100 percentage points. For the vision-language-action policy, absolute rather than relative action prediction improved insertion success by up to 70 percentage points. Skill decomposition, multi-view perception, and recovery demonstrations were associated with the strongest-performing systems, although their effects were not independently isolated. Of 67 offline metrics evaluated, only five measures of predicted-motion smoothness and directness reliably correlated with insertion success (r = -0.70 to -0.80), and only within a single policy family. These results identify representation choices as key determinants of real-world imitation-learning performance and show that offline metrics can shortlist policies, but cannot replace real-robot evaluation.

---

### Top 3: STAR: Steering Action Representations during Inference
- **Priority Score**: `135 pts` | **Published**: `2026-10-29`
- **Focus Tracks**: `#vision-language-action` `#vla`
- **Key Authors**: Guangyu Zhao, Yongchang Zhang, Haoxuan Ru et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2610.41009v1) | [PDF Fulltext](http://arxiv.org/pdf/2610.41009v1)

**Executive Abstract**:
> Vision-language-action models (VLAs) map language instructions and visual observations to robot actions, showing strong capabilities across robotic manipulation tasks. However, in our probing experiment, we find that action representations near the action output do not fully preserve task-relevant visual grounding. Motivated by this late-layer grounding gap, we introduce STAR, for STeering Action Representations, a training-free inference method for pre-trained VLAs. STAR applies an exponential moving average over late-layer residual updates, allowing later action representations to inherit object-aware update directions from earlier layers without model updates or architectural changes. It further uses recent proprioceptive states to adapt the mixing strength, using conservative mixing when execution dynamics change rapidly. Experiments on robot manipulation benchmarks show that STAR improves late-layer object awareness and increases average task success rates by 4.0 percentage points. Our code is available at https://github.com/PKU-VaLuE-Lab/STAR.

---

### Top 4: SwapBot: Tool-Centric Robot Manipulation via Interchangeable End-Effectors and Tactile Sensing
- **Priority Score**: `100 pts` | **Published**: `2026-10-29`
- **Focus Tracks**: `#tactile sensing` `#teleoperation`
- **Key Authors**: Yunchu Zhang, Ray Song, Junhan Jiao et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2610.40646v1) | [PDF Fulltext](http://arxiv.org/pdf/2610.40646v1)

**Executive Abstract**:
> Robot manipulation in everyday environments inherently involves substantial tool usage. Seemingly simple household tasks, such as cooking pan-fried tofu, require forceful cutting, delicate brushing, and precise placement using different tools under contact-rich interaction. Thus, the ability to autonomously swap and use task-appropriate tools is important for tool-centric manipulation. We introduce SwapBot, a modular, tool-centric end effector system featuring low-cost adapters that quickly convert common household tools into robot end effectors. Rather than pursuing a single universal gripper, SwapBot adopts a unified design principle that combines a fixed robot-side coupling interface with low-cost, tool-side adapters, enabling compatibility with diverse tools, including articulated ones, and multiple robot platforms. Each adapter integrates compact tactile sensors, supports fast autonomous swapping, and interfaces with an intuitive teleoperation system for efficient demonstration collection. User studies show that, during teleoperation, SwapBot reduces task completion time and operator workload. Using collected demonstrations on the robot, we train imitation learning policies to successfully perform tool-centric tasks like cooking tofu, stirring salad, flipping meat. Our ablation study shows that using tactile-augmented demonstrations improves policy performance across contact-rich skills, increasing success rates by 15 to 25 percentage points over RGB-only policies. These results highlight modular, tactile-equipped tools as a practical and extensible pathway toward robust and capable robot manipulation. Project website https://personalrobotics.github.io/SwapBot.

---

### Top 5: Contact Imitation Interface: Transferring Dexterous Skills by Showing How Contact Unfolds
- **Priority Score**: `80 pts` | **Published**: `2026-10-29`
- **Focus Tracks**: `#dexterous manipulation`
- **Key Authors**: Zhixuan Xu, Yichen Li, Bingchen Wu et al.
- **Direct Access**: [arXiv Abstract](http://arxiv.org/abs/2610.41028v1) | [PDF Fulltext](http://arxiv.org/pdf/2610.41028v1)

**Executive Abstract**:
> Robot-free human demonstrations offer a promising route to scaling dexterous manipulation data. The key challenge is to preserve the demonstrator's natural dexterity while producing contact-grounded observations and actions that transfer to robot hands. We present Contact Imitation Interface (CIMI), a framework with contact-grounded demonstration and learning interfaces. The demonstration interface combines shared contact geometry and fingertip RGB views with contact-alignment-first retargeting and reprojection of wider scene views. The learning interface introduces a hierarchical policy in which a contact-surface planner predicts relative contact-surface trajectories and a controller coordinates wrist and finger commands to improve contact alignment. CIMI combines contact-grounded observations, retargeting, and action representations, improving mean final-stage success by at least 50 percentage points over baseline policies across six hand-task pairs on LEAP and Wuji. Hardware designs and software are publicly available.

---

