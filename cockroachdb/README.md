# How to run?

```
ansible-playbook ansible/setup_cockroachdb.yml
pip install --user pdm
pdm run pytest -vv -s
ansible-playbook ansible/teardown_cockroachdb.yml
```
