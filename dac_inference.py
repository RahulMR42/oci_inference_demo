# coding: utf-8
# Copyright (c) 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import os
import oci
import time
import datetime


def print_details(msg):
    now = datetime.datetime.now()
    print(f"[{now}] - {msg}")
   

def chat(args):
    try:
        # Setup basic variables
        # Auth Config
        # TODO: Please update config profile name and use the compartmentId that has policies grant permissions for using Generative AI Service
        compartment_id = args.compartment_ocid
        CONFIG_PROFILE = os.getenv('OCI_CONFIG_PROFILE',default="DEFAULT")
        config = oci.config.from_file('~/.oci/config', CONFIG_PROFILE)

        # Service endpoint
        endpoint = f"https://inference.generativeai.{args.region}.oci.oraclecloud.com"

        with open(args.prompt_file) as fp:
            prompt = fp.read()

        generative_ai_inference_client = oci.generative_ai_inference.GenerativeAiInferenceClient(config=config, service_endpoint=endpoint, retry_strategy=oci.retry.NoneRetryStrategy(), timeout=(10,240))
        chat_detail = oci.generative_ai_inference.models.ChatDetails()

        content = oci.generative_ai_inference.models.TextContent()
        content.text = prompt
        message = oci.generative_ai_inference.models.Message()
        message.role = "USER"
        message.content = [content]

        chat_request = oci.generative_ai_inference.models.GenericChatRequest()
        chat_request.api_format = oci.generative_ai_inference.models.BaseChatRequest.API_FORMAT_GENERIC
        chat_request.messages = [message]
        chat_request.max_tokens = args.max_token
        chat_request.temperature = 0.5
        chat_request.frequency_penalty = 1
        chat_request.presence_penalty = 0
        chat_request.top_p = 0.75
        if args.endpoint_ocid:
            chat_detail.serving_mode = oci.generative_ai_inference.models.DedicatedServingMode(endpoint_id=args.endpoint_ocid)
            eid = args.endpoint_ocid
            mid = "NA"
        else:
            chat_detail.serving_mode = oci.generative_ai_inference.models.OnDemandServingMode(model_id=args.model_ocid)
            mid = args.model_ocid
            eid = "NA"
        chat_detail.chat_request = chat_request
        chat_detail.compartment_id = compartment_id
        if not args.silent:
            print_details(f"Start of execution- Promt {args.prompt_file}")
        start = time.time()
        chat_response = generative_ai_inference_client.chat(chat_detail)
        end = time.time()
        
        if not args.silent:
            print_details(f"End of execution- Promt {args.prompt_file}")
            print("**************************Chat Result**************************")
            print(vars(chat_response))
        else:
            print(f"Prompt: {args.prompt_file}  Duration(s): {end - start} OpcId: {chat_response.headers['opc-request-id']} EndPoint: {eid} ModelId: {mid} ")

        
    except Exception as error:
        print(error)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description ='sort some integers.')
    parser.add_argument('--compartment_ocid','-c',required=True,dest="compartment_ocid",help="OCID of the compartment")
    parser.add_argument('--model_ocid','-m',dest="model_ocid",help="OCID of the model for ondemand")
    parser.add_argument('--endpoint_ocid','-e',dest="endpoint_ocid",help="Model endpoint for DAC")
    parser.add_argument('--max_token','-t',dest="max_token",default=600,type=int,help="MAX token,default is 600")
    parser.add_argument('-prompt_file','-f',dest="prompt_file",required=True,help="Prompt file")
    parser.add_argument('-service_region','-r',dest="region",default="us-chicago-1",help="Service endpoint ,defaulted for us-chicago-1")
    parser.add_argument('-silent_output','-s',dest="silent",type=bool,default=False,help="Set True to disable output and pring only the time")
    args = parser.parse_args()
    chat(args)




