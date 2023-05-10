# How to run?

```
ansible-playbook ansible/setup.yml
pip install --user pdm
pdm run pytest -vv -s
ansible-playbook ansible/teardown.yml
```
