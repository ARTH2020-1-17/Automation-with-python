

import os
import subprocess as sp
from termcolor import colored

#print(colored('hello', 'red'), colored('world', 'green'))


NAMENODE_DIR_PATH = ''
DATANODE_DIR_PATH = ''


def is_hadoop_installed():
    '''
        Function checks the hadoop is intalled or not.
        return True if hadoop found otherwise False
    '''
    return_code = os.system('hadoop version')
    if return_code != 0 :
        return False
    else: 
        return True

def is_java_installed():
    '''
        Function checks the java is intalled or not.
        return True if java found otherwise False
    '''
    return_code = os.system('java -version')
    if return_code != 0 :
        return False
    else:   
        return True

def install_hadoop_setup():
    '''
        Install hadoop and java 
        return True if hadoop installtion sucessfull  otherwise False
    '''
    installation_status= True    #to check installation in successfull or not
    if is_java_installed() == False:    #if java is not installed
        print(colored('Installing Java ...','green'))
        return_code = os.system('rpm  -ivh  jdk-8u171-linux-x64.rpm')
        if return_code !=0 :
            print(colored("ERROR: Failed to install java"))
            installation_status = False
        else:
            print(colored("Java installed successfully.",'green'))
    else:
        print(colored('Java is already installed.','green'))


    if is_hadoop_installed() == False:
        print(colored('Hadoop Not Found.\n','red'),colored('Installing Hadoop...','green'))
        return_code = os.system('rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force')
        if return_code !=0 :
            print(colored("ERROR: Failed to install hadoop"))
            installation_status = False
        else:
            print(colored("Hadoop installed successfully.",'green'))
    else:
        print(colored('Hadoop Found.','green'))
    
    return installation_status

#hdfs files

HDFS_SITE_FILE='''
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<configuration>
<property>
<name>dfs.{node_type}.dir</name>
<value>{folder_path}</value>
</property>

</configuration>
'''

CORE_SITE_FILE='''
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{ip_address}:9001</value>
</property>
</configuration>
'''


def configure_namenode():
    '''
        Function to setup Name node[master node].
        create directory if not
        Edit hdfs-site.xml 
        Edit core-site.xml
        Format name node
        Start name node
    '''
    configuration_status = True
    dir_path = ''
    if NAMENODE_DIR_PATH == '':
        print(colored('Name Node Directory is not set. Do you want to set it  to continue?[Y/n]','green'))
        choice = input()
        if (choice == "N" or choice == "n"):
            print(colored('Can not process... Set Name node directory path to continue...','red'))
            configuration_status = False
            return configuration_status
        else:
            dir_path = input(colored('Enter Name node directory path','yellow'))
            return_code = os.system('mkdir -p %s'%dir_path)
            if return_code !=0:
                print(colored("Error: can not create directory at given path. Make sure you are giving proper path.",'red'))
    
    #edit hdfs-site.xml 
    print("Editing hdfs-site.html")
    hdfs_site = HDFS_SITE_FILE.format(node_type='name',folder_path=dir_path)
    return_code =  os.system('cat > /etc/hadoop/hdfs-site.xml << EOL {}'.format(hdfs_site))
    if return_code !=0:
        configuration_status = False
        print(colored('Error: can not create hdfs-site.xml file properly','red'))
        return configuration_status
    else:
        print(colored("Configured hdfs-site.xml file successfully."))

    #edit core-site.xml 
    print(colored('Do you want to configure hadoop for public ?[y/N]','yellow'))
    choice = input()
    if (choice == 'N' or choice == 'n'):
        ip='localhost'
    else:
        ip='0.0.0.0'
    core_site = CORE_SITE_FILE.format(ip_address=ip)
    return_code = os.system('cat > /etc/hadoop/core-site.xml << EOL {}'.format(core_site))
    if return_code !=0:
        configuration_status = False
        print(colored('Error: can not create core-site.xml file properly','red'))
        return configuration_status
    else:
        print(colored("Configured core-site.xml file successfully."))

    #format name node
    print(colored('Formating Name Node...','magenta'))
    return_code = os.system('hadoop namenode -format')
    if return_code != 0:
        print(colored("Error: Can not able to format.",'red'))
        return False
    else:
        print(colored('Name node formated successfully','green'))
    
    #start name node
    print(colored('Starting Name Node...','magenta'))
    return_code = os.system('hadoop-daemon.sh start namenode')
    if return_code != 0:
        print(colored("Error: Something went wrong. Can not able to start namenode service",'red'))
        configuration_status = False
        return configuration_status
    else:
        print(colored('Name node started successfully','green'))
    return configuration_status


def configure_datanode():
    '''
        Function to setup data node[slave node].
        create directory if not
        Edit hdfs-site.xml 
        Edit core-site.xml
        Start data node
    '''
    configuration_status = True
    dir_path = ''
    if DATANODE_DIR_PATH == '':
        print(colored('Data Node Directory is not set. Do you want to set it  to continue?[Y/n]','green'))
        choice = input()
        if (choice == "N" or choice == "n"):
            print(colored('Can not process... Set Data node directory path to continue...','red'))
            configuration_status = False
            return configuration_status
        else:
            dir_path = input(colored('Enter data node directory path','yellow'))
            return_code = os.system('mkdir -p %s'%dir_path)
            if return_code !=0:
                print(colored("Error: can not create directory at given path. Make sure you are giving proper path.",'red'))
    
    #edit hdfs-site.xml 
    print("Editing hdfs-site.html")
    hdfs_site = HDFS_SITE_FILE.format(node_type='data',folder_path=dir_path)
    return_code =  os.system('cat > /etc/hadoop/hdfs-site.xml << EOL {}'.format(hdfs_site))
    if return_code !=0:
        configuration_status = False
        print(colored('Error: can not create hdfs-site.xml file properly','red'))
        return configuration_status
    else:
        print(colored("Configured hdfs-site.xml file successfully."))

    #edit core-site.xml 
    print(colored('Enter name node IP address.','yellow'))
    ip = input()
    core_site = CORE_SITE_FILE.format(ip_address=ip)
    return_code = os.system('cat > /etc/hadoop/core-site.xml << EOL {}'.format(core_site))
    if return_code !=0:
        configuration_status = False
        print(colored('Error: can not create core-site.xml file properly','red'))
        return configuration_status
    else:
        print(colored("Configured core-site.xml file successfully."))

    #start data node node
    print(colored('Starting Data Node...','magenta'))
    return_code = os.system('hadoop-daemon.sh start datanode')
    if return_code != 0:
        print(colored("Error: Something went wrong. Can not able to start datanode service",'red'))
        configuration_status = False
        return configuration_status
    else:
        print(colored('Data node started successfully','green'))

    return configuration_status



def configure_client():
    '''
        Function to setup Client node in hdfs cluster
    '''
    configuration_status = True
    
    #edit core-site.xml 
    print(colored('Enter name node IP address.','yellow'))
    ip = input()
    core_site = CORE_SITE_FILE.format(ip_address=ip)
    return_code = os.system('cat > /etc/hadoop/core-site.xml << EOL {}'.format(core_site))
    if return_code !=0:
        configuration_status = False
        print(colored('Error: can not create core-site.xml file properly','red'))
        return configuration_status
    else:
        print(colored("Configured core-site.xml file successfully."))

    return configuration_status



def get_report():
    '''
        function to print hdfs report 
    '''
    return_code= os.system('hadoop dfsadmin -report')
    if return_code !=0 :
        print(colored('Something went wrong...','red'))

def put_file():
    #Put file in hadoop cluster
    file_path = input("Type the Location/name of file: ")
    return_code = os.system("hadoop fs -put {}".format(file_path))
    if return_code != 0:
        print(colored("Error: can not put file in hdfs cluster. check file path properly",'red'))
        return False
    else:
        print(colored("file put successfully in clutser",'green'))
    return True

def list_files():
    #Gives all the files present in our hadoop cluster

    return_code = os.system("hadoop fs -ls /")
    if return_code != 0:
        print(colored("Error: can not list files in hdfs cluster. ",'red'))
        return False
    return True

def read_file():
    #Read the file from cluster
    file_name = input("Type which file you want to read: ")
    return_code = os.system("hadoop fs -cat /{}".format(file_name))
    if return_code != 0:
        print(colored("Error: can not put file in hdfs cluster. check file path properly",'red'))
        return False
    else:
        print(colored("file put successfully in clutser",'green'))
    return True

def hadoop():
    print(colored("Welcome to hadoop menu..","yellow"))
    while(True):
        print('Services - ')
        print('1. Install hadoop')
        print('2. Configure Namenode')
        print('3. Configure Datanode')
        print('4. Configure Client')
        print('5. Hadoop report')
        print('6. Hadoop list files')
        print('7. Read file from cluster')
        print('8. Put file in cluster')
        print('9. Exit')

        service = int(input('Enter here : '))
        if service == 1:
            install_hadoop_setup()
        elif service == 2:
            configure_namenode()
        elif service == 3:
            configure_datanode()
        elif service == 4:
            configure_client()
        elif service == 5:
            get_report()
        elif service == 6:
            list_files()
        elif service == 7:
            read_file()
        elif service == 8:
            put_file()
        else : 
            print(colored("Exit.","magenta"))
            exit()

#hadoop()