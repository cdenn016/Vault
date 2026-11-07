---
type: paper
title: "Learning to Schedule Communication in Multi-agent Reinforcement Learning"
aliases: ["SchedNet", "Kim et al. 2019 communication scheduling"]
authors: ["Daewoo Kim", "Sangwoo Moon", "David Hostallero", "Wan Ju Kang", "Taeyoung Lee", "Kyunghwan Son", "Yung Yi"]
year: 2019
venue: "International Conference on Learning Representations"
arxiv: "1902.01554"
url: "https://arxiv.org/abs/1902.01554v1"
version: "ICLR 2019 conference paper; author PDF bearing arXiv v1, 2019-02-05"
tags: [cluster/multi-agent, cluster/attention, project/multi-agent, project/transformer, field/cs-ml]
created: 2026-11-07
updated: 2026-11-07
---

# Learning to Schedule Communication in Multi-agent Reinforcement Learning

> [!info] Citation
> Kim, D., Moon, S., Hostallero, D., Kang, W. J., Lee, T., Son, K., and Yi, Y. (2019). *Learning to Schedule Communication in Multi-agent Reinforcement Learning*. ICLR 2019. [Author PDF](https://yung-web.github.io/home/Publication/Conference/learning%20to%20schedule.pdf); [arXiv record](https://arxiv.org/abs/1902.01554v1).

[Local author PDF](../pdfs/kim-2019-schednet.pdf), 17 pages; retrieved November 7, 2026. It carries the February 5, 2019 arXiv v1 footer and ICLR publication header.

## TL;DR

SchedNet jointly learns message encoders, transmission priorities, and action policies when only a limited number of agents can broadcast.

## Problem & setting

Agents have partial observations and a shared reward. A shared medium limits message size and simultaneous senders. Sections 2.2 and 3 distinguish these communication constraints from partial observability.

## Method

An agent maps its observation into a message and a scalar scheduling weight. A supplied Top($k$) or Softmax($k$) rule grants broadcast access. Actions condition on local observations and admitted messages. Centralized critics train encoders, action selectors, and weight generators; execution uses local modules and medium-access scheduling. The nondifferentiable scheduler motivates distinct training paths for priorities and message/action modules.

## Key results

Cooperative navigation and predator–prey experiments compare learned scheduling with round robin, no communication, and full communication. Improvements concern the tested observation asymmetries and communication budgets; they do not establish a general scheduling optimum.

## Relevance to this research

[[Communication-constrained inference]] should distinguish access selection from payload construction. Selected agents broadcast; SchedNet does not choose a separate recipient for each transmission. Its shared-return training is not an [[Expected Free Energy]] derivation. [[wang-2020-information-bottleneck-communication]] adds a related compression-and-scheduling formulation.

## Cross-links

[[Active inference communication and collective boundaries]]; [[Attention Mechanism]].

## BibTeX

```bibtex
@inproceedings{kim2019SchedNet,
  author = {Kim, Daewoo and Moon, Sangwoo and Hostallero, David and Kang, Wan Ju and Lee, Taeyoung and Son, Kyunghwan and Yi, Yung},
  title = {Learning to Schedule Communication in Multi-agent Reinforcement Learning},
  booktitle = {International Conference on Learning Representations},
  year = {2019},
  eprint = {1902.01554},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/1902.01554v1}
}
```
