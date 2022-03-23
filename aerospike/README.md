# How to run?

```
ansible-playbook ansible/setup_aerospike.yml
pip install --user pdm
pdm run pytest -vv -s
ansible-playbook ansible/teardown_aerospike.yml
```
