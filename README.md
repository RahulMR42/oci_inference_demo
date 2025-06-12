# oci_inference_demo
A sample python script to run inference with DAC or On demand 

### Usage

```
$$ python inference.py -h
usage: inference.py [-h] --compartment_ocid COMPARTMENT_OCID [--model_ocid MODEL_OCID] [--endpoint_ocid ENDPOINT_OCID] [--max_token MAX_TOKEN]
                        -prompt_file PROMPT_FILE [-service_region REGION] [-silent_output SILENT]

sort some integers.

options:
  -h, --help            show this help message and exit
  --compartment_ocid COMPARTMENT_OCID, -c COMPARTMENT_OCID
                        OCID of the compartment
  --model_ocid MODEL_OCID, -m MODEL_OCID
                        OCID of the model for ondemand
  --endpoint_ocid ENDPOINT_OCID, -e ENDPOINT_OCID
                        Model endpoint for DAC
  --max_token MAX_TOKEN, -t MAX_TOKEN
                        MAX token,default is 600
  -prompt_file PROMPT_FILE, -f PROMPT_FILE
                        Prompt file
  -service_region REGION, -r REGION
                        Service endpoint ,defaulted for us-chicago-1
  -silent_output SILENT, -s SILENT
                        Set True to disable output and pring only the time
```

### Run with Endpoint 

```
python dac.py  -c "OCID OF OCI COMPARTMENT" -e "END POINT OCID" -t <MAX TOKEN> -f "prompt text"
```

### Run with ondemand model id

```
python dac.py  -c "OCID OF OCI COMPARTMENT " -t <MAX TOKEN> -f "promptfile.txt"  -m <OCID of the model>
```

### An example of running 100 occurance against 5 prompts such as 1.txt ...5.txt via cloud shell.

```
for i in $(seq 1 100); do  for i in $(seq 1 5); do python inference.py  -c "<Compartment OCID>" -e "<Endpoint OCID>" -t 1000 -f "${i}.txt" -t 4000 -s true |tee -a /tmp/output.txt;echo "......------------......."; done; done
```
