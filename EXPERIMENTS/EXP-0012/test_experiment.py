import unittest

from experiment import DeterministicWorld, MemoryAgent, OrganismAgent


class Exp0012Controls(unittest.TestCase):
    def test_world_is_deterministic(self):
        a = DeterministicWorld(7)
        b = DeterministicWorld(7)
        for _ in range(a.total_steps):
            self.assertEqual(a.observation(), b.observation())
            obs_a = a.observation()
            obs_b = b.observation()
            self.assertEqual(obs_a, obs_b)
            action = obs_a.relation
            self.assertEqual(a.step(action), b.step(action))

    def test_same_observable_spaces(self):
        self.assertEqual(set(MemoryAgent(1).q.keys()), {0, 1})
        self.assertEqual(set(OrganismAgent(1).q.keys()), {0, 1})

    def test_affect_is_derived_from_prediction_error(self):
        agent = OrganismAgent(1)
        self.assertEqual(agent.tension, 0.0)
        obs = DeterministicWorld(1).observation()
        agent.observe(obs, 0, -1.0)
        self.assertGreater(agent.tension, 0.0)
        self.assertGreater(agent.uncertainty, 0.0)

    def test_affect_ablation_disables_affective_modulation(self):
        agent = OrganismAgent(1, affect_enabled=False)
        base = agent.epsilon
        agent.observe(DeterministicWorld(1).observation(), 0, -1.0)
        self.assertEqual(agent.tension, 0.0)
        self.assertEqual(agent.uncertainty, 0.0)
        self.assertLessEqual(agent.exploration_probability(), base)


if __name__ == "__main__":
    unittest.main()
