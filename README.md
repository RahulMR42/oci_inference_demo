# oci_inference_demo
A sample python script to run inference with DAC or On demand 

### Usage

```
$$ python dac_inference.py -h
usage: dac_inference.py [-h] --compartment_ocid COMPARTMENT_OCID [--model_ocid MODEL_OCID] [--endpoint_ocid ENDPOINT_OCID] [--max_token MAX_TOKEN]
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

