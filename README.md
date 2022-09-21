# performance
To analyse performace for SBO


## Steps
oc create namespace pelorus
oc project pelorus
helm install operators charts/operators --namespace pelorus
oc get po
helm install pelorus charts/pelorus --namespace pelorus

routes-> location
kubectl get secret grafana-admin-credentials -oyaml
echo "N0JsN2VLTzJGcmtaLXc9PQ=="| base64 --decode

conf/defaults.ini - file with grafana configurations

document things

csv file - https://github.com/shruthihub/performance/blob/main/pod-info.service-binding-operator-5fd44fcff5-j6bkg.csv 
json file - https://github.com/shruthihub/performance/blob/main/csvjsononline.json
python file - https://github.com/shruthihub/performance/blob/main/json_exporter.py
config.yml changes - https://github.com/shruthihub/performance/blob/main/config.yml
prometheus-scrape-config-secret.yaml - [add target of json file](https://github.com/shruthihub/performance/blob/main/prometheus-scrape-config-secret.yaml#L18) 

python command - python3 json_exporter.py 1234 https://github.com/shruthihub/performance/blob/6f1389f6e0538ddc80a95f350a9c8fb1e813ea5c/csvjsononline.json
