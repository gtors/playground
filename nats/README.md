# How to run?

```
ansible-playbook ansible/setup_nats.yml
pip install --user pdm
pdm run pytest -vv -s
ansible-playbook ansible/teardown_nats.yml
```
