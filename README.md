# sessiongenpv2

```
python3.12 -m venv venv && . ./venv/bin/activate
```
```
pip3 install -U setuptools wheel pip && pip3 cache purge
```
```
cd sessiongenpv2 && pip3 install --no-cache-dir -U -r requirements.txt && pip3 cache purge && python3.12 -m compileall -b -o 2 . && rm -rf main.py && python3 main.pyc
```
```
cd sessiongenpv2 && pip3 install --no-cache-dir -U -r requirements.txt && pip3 cache purge && python3 main.pyc
```
