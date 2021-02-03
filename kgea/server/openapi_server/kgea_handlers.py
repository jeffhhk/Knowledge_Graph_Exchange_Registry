import os
from pathlib import Path

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from flask import abort, render_template


import jinja2
from string import Template

import boto3

from botocore.exceptions import ClientError

#############################################################
# Application Configuration
#############################################################

from .kgea_config import s3_client, resources

#############################################################
# Site Controller Handlers
#
# Insert imports and return calls into site_controller.py:
#
# from ..kge_handlers import (
#     kge_client_authentication,
#     kge_login,
#     kge_logout,
#     get_kge_landing_page,
#     get_kge_home
# )
#############################################################


def kge_client_authentication(code):  # noqa: E501
    """Process client authentication

     # noqa: E501

    :param code:
    :type code: str

    :rtype: str
    """
    return 'do some magic!'


def kge_login():  # noqa: E501
    """Process client user login

     # noqa: E501

    :rtype: None
    """
    return 'do some magic!'


def kge_logout():  # noqa: E501
    """Process client user logout

     # noqa: E501

    :rtype: None
    """
    return 'do some magic!'

# TODO: Login/logout redirections? using flask.redirect(location, code=302, Response=None)


def get_kge_home():  # noqa: E501
    """Get default landing page

     # noqa: E501

    :rtype: str
    """
    return render_template('home.html')


def get_kge_landing_page(session=None):  # noqa: E501
    """Get default public landing page (when the site visitor is not authenticated)

     # noqa: E501

    :param session:
    :type session: str

    :rtype: str
    """
    return 'do some magic!'

#############################################################
# Provider Controller Handler
#
# Insert import and return call into provider_controller.py:
#
# from ..kge_handlers import kge_access
#############################################################


def kge_access(kg_name):  # noqa: E501
    """Get KGE File Sets

     # noqa: E501

    :param kg_name: Name label of KGE File Set whose files are being accessed
    :type kg_name: str

    :rtype: Dict[str, Attribute]
    """
    
    object_location = Template('$DIRECTORY_NAME/$KG_NAME/$CONTENT_TYPE/').substitute(
        DIRECTORY_NAME='kge-data',
        KG_NAME=kg_name,
        CONTENT_TYPE='content'
    )
    
    def create_presigned_url(bucket, object_name, expiration=3600):
        """Generate a presigned URL to share an S3 object

        :param bucket: string
        :param object_name: string
        :param expiration: Time in seconds for the presigned URL to remain valid
        :return: Presigned URL as string. If error, returns None.
        """
        
        # Generate a presigned URL for the S3 object
        # TODO: https://stackoverflow.com/a/52642792
        # s3_client = boto3.client('s3', config=Config(signature_version='s3v4'))
        try:
            response = s3_client.generate_presigned_url('get_object',
                                                        Params={'Bucket': bucket,
                                                                'Key': object_name},
                                                        ExpiresIn=expiration)
        except ClientError as e:
            print(e)
            return None
        
        # The response contains the presigned URL
        return response
    
    def kg_files_in_location(bucket_name, object_location):
        # s3_client = boto3.client('s3', config=Config(signature_version='s3v4'))
        
        # TODO: Warning! Doesn't scale very well, looks somewhat unsafe. What other options do we have to query the bucket?
        bucket_listings = [e['Key'] for p in s3_client.get_paginator("list_objects_v2").paginate(Bucket=bucket_name) for
                           e in p['Contents']]
        object_matches = [object_name for object_name in bucket_listings if object_location in object_name]
        
        return object_matches
    
    # Listings Approach
    # - Introspect on Bucket
    # - Create URL per Item Listing
    # - Send Back URL with Dictionary
    # OK in case with multiple files (alternative would be, archives?). A bit redundant with just one file.
    # TODO: convert into redirect approach with cross-origin scripting?
    kg_files = kg_files_in_location(bucket_name=resources['bucket'], object_location=object_location)
    kg_listing = dict(
        map(lambda kg_file: [Path(kg_file).stem, create_presigned_url(resources['bucket'], kg_file)], kg_files))
    return kg_listing


#############################################################
# Content Controller Handler
#
# Insert import and return call into content_controller.py:
#
# from .kge_handlers import kge_knowledge_map
#############################################################


def kge_knowledge_map(kg_name):  # noqa: E501
    """Get supported relationships by source and target

     # noqa: E501

    :param kg_name: Name label of KGE File Set whose knowledge graph content metadata is being reported
    :type kg_name: str

    :rtype: Dict[str, Dict[str, List[str]]]
    """
    
    object_location = Template('$DIRECTORY_NAME/$KG_NAME/$CONTENT_TYPE/').substitute(
        DIRECTORY_NAME='kge-data',
        KG_NAME=kg_name,
        CONTENT_TYPE='metadata'
    )
    
    def create_presigned_url(bucket, object_name, expiration=3600):
        """Generate a presigned URL to share an S3 object

        :param bucket: string
        :param object_name: string
        :param expiration: Time in seconds for the presigned URL to remain valid
        :return: Presigned URL as string. If error, returns None.
        """
        
        # Generate a presigned URL for the S3 object
        # TODO: https://stackoverflow.com/a/52642792
        # s3_client = boto3.client('s3', config=Config(signature_version='s3v4'))
        try:
            response = s3_client.generate_presigned_url('get_object',
                                                        Params={'Bucket': bucket,
                                                                'Key': object_name},
                                                        ExpiresIn=expiration)
        except ClientError as e:
            print(e)
            return None
        
        # The response contains the presigned URL
        return response
    
    def kg_files_in_location(bucket_name, object_location):
        #s3_client = boto3.client('s3', config=Config(signature_version='s3v4'))
        
        # TODO: Warning! Doesn't scale very well, looks somewhat unsafe. What other options do we have to query the bucket?
        bucket_listings = [e['Key'] for p in s3_client.get_paginator("list_objects_v2").paginate(Bucket=bucket_name) for
                           e in p['Contents']]
        object_matches = [object_name for object_name in bucket_listings if object_location in object_name]
        
        return object_matches
    
    # Listings Approach
    # - Introspect on Bucket
    # - Create URL per Item Listing
    # - Send Back URL with Dictionary
    # OK in case with multiple files (alternative would be, archives?). A bit redundant with just one file.
    # TODO: convert into redirect approach with cross-origin scripting?
    kg_files = kg_files_in_location(bucket_name=resources['bucket'], object_location=object_location)
    kg_listing = dict(
        map(lambda kg_file: [Path(kg_file).stem, create_presigned_url(resources['bucket'], kg_file)], kg_files))
    return kg_listing


#############################################################
# Upload Controller Handlers
#
# Insert imports and return calls into upload_controller.py:
#
# from .kge_handlers import (
#     get_kge_register_form,
#     get_kge_upload_form,
#     register_kge_file_set,
#     upload_kge_file_set,
# )
#############################################################

def get_kge_register_form(kg_name=None, submitter=None):  # noqa: E501
    """Get web form for specifying KGE File Set upload

     # noqa: E501

    :param kg_name:
    :type kg_name: str
    :param submitter:
    :type submitter: str

    :rtype: str
    """
    
    kg_name_text = kg_name
    submitter_text = submitter
    if kg_name is None:
        kg_name_text = ''
    if submitter is None:
        submitter_text = ''
    
    page = """
    <!DOCTYPE html>
    <html>

    <head>
        <title>Register Files for Knowledge Graph</title>
    </head>

    <body>
        <h1>Register Files for Knowledge Graph</h1>

        <form action="/register" method="post" enctype="application/x-www-form-urlencoded">
            KnowledgeGraph Name: <input type="text" name="kg_name" value="{{kg_name}}"><br>
            Submitter: <input type="text" name="submitter" value="{{submitter}}"><br>
            <input type="submit" value="Register">
        </form>

    </body>

    </html>
    """
    return jinja2.Template(page).render(kg_name=kg_name_text, submitter=submitter_text)


def get_kge_upload_form(kg_name):  # noqa: E501
    """Get web form for specifying KGE File Set upload

     # noqa: E501

    :param kg_name:
    :type kg_name: str

    :rtype: str
    """
    # TODO guard against absent kg_name
    # TODO guard against invalid kg_name (check availability in bucket)
    # TODO redirect to register_form with given optional param as the entered kg_name
    
    page = """
    <!DOCTYPE html>
    <html>

    <head>
        <title>Upload New File</title>
    </head>

    <body>
        <h1>Upload Files</h1>

        <form action="/upload/{{kg_name}}" method="post" enctype="multipart/form-data">
            API Files: <input type="file" name="data_file_content"><br>
            API Metadata: <input type="file" name="data_file_metadata"><br>
            <input type="submit" value="Upload">
        </form>

    </body>

    </html>
    """
    return jinja2.Template(page).render(kg_name=kg_name)


def register_kge_file_set(body):  # noqa: E501
    submitter = body['submitter']
    kg_name = body['kg_name']
    
    object_location = Template('$DIRECTORY_NAME/$KG_NAME/').substitute(
        DIRECTORY_NAME='kge-data',
        KG_NAME=kg_name
    )
    
    def location_available(bucket_name, object_key):
        """
        Guarantee that we can write to the location of the object without overriding everything

        :param bucket: The bucket
        :param object: The object in the bucket
        :return: True if the object is not in the bucket, False if it is already in the bucket
        """
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(bucket_name)
        key = object_key
        objs = list(bucket.objects.filter(Prefix=key))
        if any([w.key == key for w in objs]):
            # exists
            # invert because unavailable
            return not True
        else:
            # doesn't exist
            # invert because available
            return not False
    
    # TODO
    def create_smartapi(submitter, kg_name):
        spec = {}
        
        def convert_to_yaml(spec):
            yaml_file = lambda spec: spec
            return yaml_file(spec)
        
        yaml_file = convert_to_yaml(api_specification)
        
        return spec
    
    # TODO
    def add_to_github(api_specification):
        # using https://github.com/NCATS-Tangerine/translator-api-registry
        repo = ''
        return repo
    
    api_specification = create_smartapi(submitter, kg_name)
    url = add_to_github(api_specification)
    
    if location_available:
        if api_specification and url:
            return dict({
                "url": url,
                "api": api_specification
            })
        else:
            abort(400)
    else:
        abort(201)


def upload_kge_file_set(kg_name, data_file_content, data_file_metadata=None):  # noqa: E501
    """Upload web form details specifying a KGE File Set upload process

     # noqa: E501

    :param kg_name:
    :type kg_name: str
    :param data_file_content:
    :type data_file_content: str
    :param data_file_metadata:
    :type data_file_metadata: str

    :rtype: str
    """
    print(kg_name, data_file_content, data_file_metadata)
    object_location = Template('$DIRECTORY_NAME/$KG_NAME/').substitute(
        DIRECTORY_NAME='kge-data',
        KG_NAME=kg_name
    )
    
    def upload_file(data_file, bucket_name, object_location, content_type, override=False):
        """Upload a file to an S3 bucket

        :param file_name: File to upload
        :param bucket: Bucket to upload to
        :param object_name: S3 object name. If not specified then file_name is used
        :return: True if file was uploaded, else False
        """
        object_key = object_location + content_type + '/' + data_file.filename
        
        # Upload the file
        """ s3_client = boto3.client('s3', config=Config(
            # Don't need to set the region -
            # externally defined `aws configure`
            # default value should be used?
            # region_name='ca-central-1',
            signature_version='s3v4')
                                 )
        """

        try:
            with data_file.stream as f:
                s3_client.upload_fileobj(f, bucket_name, object_key)
        except ClientError as e:
            # TODO: replace with logger
            print(e)
            return None
        return object_key
    
    # # TODO
    # def api_registered(kg_name):
    #     return True
    #
    
    # def location_available(bucket_name, object_key):
    #     """
    #     Guarantee that we can write to the location of the object without overriding everything
    #
    #     :param bucket: The bucket
    #     :param object: The object in the bucket
    #     :return: True if the object is not in the bucket, False if it is already in the bucket
    #     """
    #     s3 = boto3.resource('s3')
    #     bucket = s3.Bucket(bucket_name)
    #     key = object_key
    #     objs = list(bucket.objects.filter(Prefix=key))
    #     if any([w.key == key for w in objs]):
    #         # exists
    #         # invert because unavailable
    #         return not True
    #     else:
    #         # doesn't exist
    #         # invert because available
    #         return not False
    
    # if api_registered(kg_name) and not location_available(bucket_name, object_location) or override:
    maybeUploadContent = upload_file(data_file_content, bucket_name=resources['bucket'], object_location=object_location,
                                     content_type="content")
    maybeUploadMetaData = None or data_file_metadata and upload_file(data_file_metadata, bucket_name=resources['bucket'],
                                              object_location=object_location, content_type="metadata")
    
    def create_presigned_url(bucket, object_name, expiration=3600):
        """Generate a presigned URL to share an S3 object

        :param bucket: string
        :param object_name: string
        :param expiration: Time in seconds for the presigned URL to remain valid
        :return: Presigned URL as string. If error, returns None.
        """
        
        # Generate a presigned URL for the S3 object
        # https://stackoverflow.com/a/52642792
        # s3_client = boto3.client('s3', config=Config(signature_version='s3v4'))
        try:
            response = s3_client.generate_presigned_url('get_object',
                                                        Params={'Bucket': bucket,
                                                                'Key': object_name},
                                                        ExpiresIn=expiration)
        except ClientError as e:
            print(e)
            return None
        
        # The response contains the presigned URL
        return response
    
    if maybeUploadContent or maybeUploadMetaData:
        response = {"content": dict({}), "metadata": dict({})}
        
        content_name = Path(maybeUploadContent).stem
        content_url = create_presigned_url(bucket=resources['bucket'], object_name=maybeUploadContent)

        if content_name in response["content"]:
            abort(400)
        else:
            response["content"][content_name] = content_url
        
        if maybeUploadMetaData:
            metadata_name = Path(maybeUploadMetaData).stem
            metadata_url = create_presigned_url(bucket=resources['bucket'], object_name=maybeUploadMetaData)
            if metadata_name not in response["metadata"]:
                response["metadata"][metadata_name] = metadata_url
            # don't care if not there since optional
        
        return response
    else:
        abort(400)
