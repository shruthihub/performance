# performance
To analyse performace for SBO


##Steps
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

csv file - /home/srp/pelorus/perfomance/performance-data/metrics/pod-info.service-binding-operator-5fd44fcff5-j6bkg.csv 
json file - https://github.com/shruthihub/performance/blob/6f1389f6e0538ddc80a95f350a9c8fb1e813ea5c/csvjsononline.json
python file - 
config.yml changes - add target of json file 

python command - python3 json_exporter.py 1234 https://github.com/shruthihub/performance/blob/6f1389f6e0538ddc80a95f350a9c8fb1e813ea5c/csvjsononline.json
