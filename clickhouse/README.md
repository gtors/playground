# How to run?

```
ansible-playbook ansible/setup_.yml
pip install --user pdm
pdm run pytest -vv -s
ansible-playbook ansible/teardown_.yml
```
