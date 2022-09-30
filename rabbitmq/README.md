# How to run?

```
ansible-playbook ansible/setup_rabbitmq.yml
pip install --user pdm
pdm run pytest -vv -s
ansible-playbook ansible/teardown_rabbitmq.yml
```
