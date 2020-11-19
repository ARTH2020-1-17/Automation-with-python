import os                                         # os module for linux commands
from pyfiglet import Figlet                       #figlet library for banner fonts 
#import subprocess as sp
from termcolor import colored
import getpass

def dockerconf():
        print("-----------DOCKER----------")
        print("1. Docker daemon start/stop/status")
        print("2. Show docker process")
        print("3. Show docker images")
        print("4. Search images on docker hub")
        print("5. Download docker image from docker hub")
        print("6. Run a docker image")
        print("7. Stop docker container")
        print("8. Delete docker image")
        command=int(input("Enter your choice: "))


        if command == 1:
            print("1.start  2.stop  3.status")
            op = int(input())
            if op == 1:
                os.system('systemctl start docker')
            elif op == 2:
                os.system('sytemctl stop docker')
            elif op == 3:
                os.system('systemctl status docker')
            else:
                print('unsupported input')
        elif command == 2:
            op = int(input('1.Recent process  2.All process'))
            if op == 1:
                os.system('docker ps')
                input()
            elif op == 2:
                os.system('docker ps -a')
                input()
            else:
                print('unsupported input')
        elif command == 3:
            os.system('docker images')
            input()
        elif command == 4:
            im = input('image name - ')
            os.system('docker search {}'.format(im))
            input()
        elif command == 5:
            im = input('image name - ')
            os.system('docker pull {}'.format(im))
            input()
        elif command == 6:
            im = input('image name - ')
            os.system('docker run -it {} &'.format(im))
            input()
        elif command == 7:
            im = input('image name - ')
            os.system('docker stop {}'.format(im))
            input()
        elif command == 8:
            im = input('image name - ')
            os.system('docker rmi {}'.format(im))
            input()
        
        else:
            print('Error')



def lvmconf():
	os.system("tput setaf 2")
	print("\t\t----------------------------------------")
	print("\t\t\t\tAVAILABLE MENUS")
	print("\t\t-----------------------------------------")
	os.system("tput setaf 7")
	print("\t\t\t1. Check available disks")
	print("\t\t\t2. Create physical volumes(PV)")
	print("\t\t\t3. Create Volume Group (VG)")
	print("\t\t\t4. Create Logical volumes(LV)")
	print("\t\t\t5. Format the created LV")
	print("\t\t\t6. Mount the LV")
	print("\t\t\t7. Extend Volume Group")
	print("\t\t\t8. Format the extende volume")
	print("\t\t\t9. To display volume group.")
	print("\t\t\t0. to display Logical volume.")
	
	os.system("tput setaf 7")
	lvm = int(input("Enter your choice : "))
	if lvm == 1:
		p = os.system('fdisk -l')
		print(p)
		input()
	elif lvm == 2:
		y = int(input("How many hard disks do you want to convert into PV:"))
		for i in range(y):
			r = str(i+1)
			p = input("Enter the name of disk no "+r+" :")
			q = os.system("pvcreate {0}".format(p))
			print(q)
			input()
	elif lvm == 3:
		a = input("Enter the name for volume group which is to be created :")
		b = input("Enter name of physical volume (please separate the names by giving space if you want to give more than one):")
		s = os.system("vgcreate {0} {1} ".format(a,b))

	elif lvm == 4:
		e = input("Enter size for LV in (G/M/T):")
		d = input("Enter name for LV :")
		f = input("Enter name of created volume group: ")
		lv = os.system("lvcreate --size {0} --name {1} {2}".format(e,d,f))
	elif lvm == 5:
		vg_nm = input("Enter Created VG name :")
		lv_nm = input("Enter Created LV name :")
		frmt = os.system("mkfs.ext4 /dev/{0}/{1}".format(vg_nm,lv_nm))
	elif lvm == 6:
		vg = input("Enter created name of volume group.")
		ln = input("Enter Created LV name :")
		dr = input("Enter name to create directory:")
		os.system("mkdir /{0}".format(dr))	
		print("mounting your partition on created directory...")
		os.system("mount /dev/{0}/{1} /{2}".format(vg,ln,dr))
		print("partition mounted successfully")
		input()
	elif lvm == 7:
		u = input("Howm much size do you want to extend ,Enter size in (G/M/T):")
		w = input("Enter name of created volume group: ")
		v = input("Enter name of created LV :")
		resize = os.system("lvextend --size +{0}  /dev/{1}/{2}".format(u,w,v))
		print(resize)
		input()
	elif lvm == 8:
		r_v = input("Enter name of created volume group: ")
		r_l = input("Enter name of created LV :")
		re_frmt = os.system("resize2fs /dev/{0}/{1}".format(r_v,r_l))
		print(re_frmt)
		input()
	elif lvm == 9:
		vgname=input("enter vg name:")
		v_disp = os.system("vgdisplay {0}".format(vgname))
		print(v_disp)
		input()
	elif lvm == 0:
		vgname2=input("Enter vg name:")
		lvname=input("Enter lv name:")
		lv_display=os.system("lvdisplay {}/{}".format(vgname2,lvname))
		print(lv_display)
		input()
	else:
		print("invalid input chech once again.")
		input()


def awsconf():
    print('--Services--')
    print('EC2')
    print('EBS')
    print('S3 ')
    aws_ser = input('Enter here : ')
    if aws_ser == 'EC2' or 'ec2':
        ec2conf()
    elif aws_ser == 'EBS' or 'ebs':
        ebsconf()
    elif aws_ser == 'S3' or 's3':
        s3conf()
    else:
        print('unsupported input')


def ec2conf():
    print("-----------EC2----------")
    print("1. Create/Delete Key Pair")
    print("2. Create/Delete Security group")
    print("3. EC2 instance start/stop/terminate")
    print("4. Show all instances ")
    print("5. Create new Instance")
    command = int(input('\nEnter your choice - '))
    if command == 1:
        kp = int(input('1.Create  2.Delete '))
        if kp == 1:
            key_name = input("Enter key name : ")
            os.system('aws ec2 create-key-pair --key-name {0}'.format(key_name))
        elif kp == 2:
            key_name = input("Enter key name : ")
            os.system('aws ec2 delete-key-pair --key-name {0}'.format(key_name))
        else:
            print('unsupported input')
    elif command == 2:
        sg = int(input('1.Create  2.Delete '))
        if sg == 1:
            se_group_name = input("Enter name for security group : ")
            se_disc = input("Enter description for security group : ")
            os.system(
                'aws ec2 create-security-group --group-name {0} --description {1}'.format(se_group_name, se_disc))
        elif sg == 2:
            se_grp_id = input("Enter id of security group :")
            os.system('aws ec2 delete-security-group --group-id{0}'.format(se_grp_id))
        else:
            print('unsupported input')
    elif command == 3:
        ins_id = input(" Enter Instance ID : ")
        op = int(input('1.start  2.stop  3.terminate'))
        if op == 1:
            os.system('aws ec2 start-instances --instance-ids {0}'.format(ins_id))
        elif op == 2:
            os.system('aws ec2 stop-instances --instance-ids {0}'.format(ins_id))
        elif op == 3:
            os.system('aws ec2 terminate-instances --instance-ids {0}'.format(ins_id))
        else:
            print('unsupported input')
    elif command == 4:
        l = os.system('aws ec2 describe-instances')
        print(l)
    elif command == 5:
        img_id = input("Enter image id : ")
        img_type = input("Enter image type : ")
        subnet_id = input("Enter subnetId : ")
        se_id = input("Enter security group id : ")
        key_name = input("Enter created  key name : ")
        os.system(
            'aws ec2 run-instances --image-id {0} --instance-type {1} --subnet-id {2} --security-group-id {3} --key-name {4}'.format(
                img_id, img_type, subnet_id, se_id, key_name))
    else:
        print('unsupported input')


def ebsconf():
    print("-----------EBS----------")
    print("1. Create EBS volume")
    print("2. Attach EBS volume to EC2 instance")
    command = int(input('\nEnter your choice - '))
    if command == 1:
        vt = input("Enter the type of volume : ")
        size = input("Enter the size of volume :")
        zone = input("Enter the name of avaiability zone :")
        os.system(
            'aws ec2 create-volume --volume-type {0} --size {1}  --availability-zone {2}'.format(vt, size, zone))
    elif command == 2:
        vol_id = input("Enter volume id: ")
        instance_id = input("Enter instance id : ")
        dev_name = input("Enter device name or drive name : ")
        os.system('aws ec2 attach-volume --volume-id {0} --instance-id {1} --device {2}'.format(vol_id, instance_id,
                                                                                                   dev_name))
    else:
        print('unsupported input')


def s3conf():
	print("-----------S3----------")
	print("1. Create Bucket")
	print("2. List buckets and objects")
	print("3. Create Object")
	print("4. Delete Bucket")
	print("5. Delete Object")
	command = int(input('\nEnter your choice - '))
	if command == 1:
		buck_name = input("Enter unique bucket name : ")
		s = os.system('aws s3 mb s3://{}'.format(buck_name))
		print(s)
	elif command == 2:
		s = os.system('aws s3 ls')
		print(s)
	elif command == 3:
		s = os.system('aws s3 sync')
		print(s)
	elif command == 4:
		buck_name = input("Enter bucket name : ")
		s = os.system('aws s3 rb s3://{}'.format(buck_name))
		print(s)
	elif command == 5:
		buck_name = input("Enter bucket name : ")
		obj_name = input("Enter object name :")
		s = os.system("aws s3 rm s3://{0}{1}".format(buck_name,obj_name))

# print(colored('hello', 'red'), colored('world', 'green'))


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
	installation_status=True
	# to check installation in successfull or not
	if is_java_installed() == False:  # if java is not installed
		print(colored('Installing Java ...' ,'green'))
		return_code = os.system('rpm  -ivh  jdk-8u171-linux-x64.rpm')

		if return_code !=0 :
			print(colored("ERROR: Failed to install java"))
			installation_status = False
		else:
			print(colored("Java installed successfully." ,'green'))
	else:
		print(colored('Java is already installed.' ,'green'))


	if is_hadoop_installed() == False:
		print(colored('Hadoop Not Found.\n' ,'red') ,colored('Installing Hadoop...' ,'green'))
		return_code = os.system('rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force')
		if return_code !=0 :
			print(colored("ERROR: Failed to install hadoop"))
			installation_status = False
		else:
			print(colored("Hadoop installed successfully." ,'green'))
	else:
		print(colored("Hadoop Found." ,'green')) 
		return installation_status


# hdfs files

HDFS_SITE_FILE ='''
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<configuration>
<property>
<name>dfs.{node_type}.dir</name>
<value>{folder_path}</value>
</property>

</configuration>
'''

CORE_SITE_FILE ='''
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
		print(colored('Name Node Directory is not set. Do you want to set it  to continue?[Y/n]' ,'green'))
	choice = input()
	if (choice == "N" or choice == "n"):
		print(colored('Can not process... Set Name node directory path to continue...' ,'red'))
		configuration_status = False
		return configuration_status
	else:
		dir_path = input(colored('Enter Name node directory path' ,'yellow'))
		return_code = os.system('mkdir -p %s ' %dir_path)
		if return_code !=0:
			print(colored("Error: can not create directory at given path. Make sure you are giving proper path."
							,'red'))

	# edit hdfs-site.xml
	print("Editing hdfs-site.html")
	hdfs_site = HDFS_SITE_FILE.format(node_type='name' ,folder_path=dir_path)
	return_code =  os.system('cat > /etc/hadoop/hdfs-site.xml << EOL {}'.format(hdfs_site))
	if return_code !=0:
		configuration_status = False
		print(colored('Error: can not create hdfs-site.xml file properly' ,'red'))
		return configuration_status
	else:
		print(colored("Configured hdfs-site.xml file successfully."))

	# edit core-site.xml
	print(colored('Do you want to configure hadoop for public ?[y/N]' ,'yellow'))
	choice = input()
	if (choice == 'N' or choice == 'n'):
		ip = 'localhost'
	else:
		ip ='0.0.0.0'
	core_site = CORE_SITE_FILE.format(ip_address=ip)
	return_code = os.system('cat > /etc/hadoop/core-site.xml << EOL {}'.format(core_site))
	if return_code != 0:
		configuration_status = False
		print(colored('Error: can not create core-site.xml file properly' ,'red'))
		return configuration_status
	else:
		print(colored("Configured core-site.xml file successfully."))

	# format name node
	print(colored('Formating Name Node...' ,'magenta'))
	return_code = os.system('hadoop namenode -format')
	if return_code != 0:
		print(colored("Error: Can not able to format." ,'red'))
		return False
	else:
		print(colored('Name node formated successfully' ,'green'))

	# start name node
	print(colored('Starting Name Node...' ,'magenta'))
	return_code = os.system('hadoop-daemon.sh start namenode')
	if return_code != 0:
		print(colored("Error: Something went wrong. Can not able to start namenode service" ,'red'))
		configuration_status = False
		return configuration_status
	else:
		print(colored('Name node started successfully' ,'green'))
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
		print(colored('Data Node Directory is not set. Do you want to set it  to continue?[Y/n]' ,'green'))
		choice = input()
		if (choice == "N" or choice == "n"):
			print(colored('Can not process... Set Data node directory path to continue...' ,'red'))
			configuration_status = False
			return configuration_status
		else:
			dir_path = input(colored('Enter data node directory path' ,'yellow'))
			return_code = os.system('mkdir -p %s ' %dir_path)
			if return_code != 0:
				print(colored("Error: can not create directory at given path. Make sure you are giving proper path."
							,'red'))

	# edit hdfs-site.xml
	print("Editing hdfs-site.html")
	hdfs_site = HDFS_SITE_FILE.format(node_type='data' ,folder_path=dir_path)
	return_code =  os.system('cat > /etc/hadoop/hdfs-site.xml << EOL {}'.format(hdfs_site))
	if return_code != 0:
		configuration_status = False
		print(colored('Error: can not create hdfs-site.xml file properly' ,'red'))
		return configuration_status
	else:
		print(colored("Configured hdfs-site.xml file successfully."))

	# edit core-site.xml
	print(colored('Enter name node IP address.' ,'yellow'))
	ip = input()
	core_site = CORE_SITE_FILE.format(ip_address=ip)
	return_code = os.system('cat > /etc/hadoop/core-site.xml << EOL {}'.format(core_site))
	if return_code != 0:
		configuration_status = False
		print(colored('Error: can not create core-site.xml file properly' ,'red'))
		return configuration_status
	else:
		print(colored("Configured core-site.xml file successfully."))

	# start data node node
	print(colored('Starting Data Node...' ,'magenta'))
	return_code = os.system('hadoop-daemon.sh start datanode')
	if return_code != 0:
		print(colored("Error: Something went wrong. Can not able to start datanode service" ,'red'))
		configuration_status = False
		return configuration_status
	else:
		print(colored('Data node started successfully' ,'green'))

	return configuration_status



def configure_client():
	'''
	Function to setup Client node in hdfs cluster
	'''
	configuration_status = True

	# edit core-site.xml
	print(colored('Enter name node IP address.' ,'yellow'))
	ip = input()
	core_site = CORE_SITE_FILE.format(ip_address=ip)
	return_code = os.system('cat > /etc/hadoop/core-site.xml << EOL {}'.format(core_site))
	if return_code != 0:
		configuration_status = False
		print(colored('Error: can not create core-site.xml file properly' ,'red'))
		return configuration_status
	else:
		print(colored("Configured core-site.xml file successfully."))

	return configuration_status



def get_report():
	'''
	function to print hdfs report
	'''
	return_code= os.system('hadoop dfsadmin -report')
	if return_code != 0 :
		print(colored('Something went wrong...' ,'red'))

def put_file():
	# Put file in hadoop cluster
	file_path = input("Type the Location/name of file: ")
	return_code = os.system("hadoop fs -put {}".format(file_path))
	if return_code != 0:
		print(colored("Error: can not put file in hdfs cluster. check file path properly" ,'red'))
		return False
	else:
		print(colored("file put successfully in clutser" ,'green'))
		return True

def list_files():
	# Gives all the files present in our hadoop cluster

	return_code = os.system("hadoop fs -ls /")
	if return_code != 0:
		print(colored("Error: can not list files in hdfs cluster. " ,'red'))
		return False
	else:
		return True

def read_file():
	# Read the file from cluster
	file_name = input("Type which file you want to read: ")
	return_code = os.system("hadoop fs -cat /{}".format(file_name))
	if return_code != 0:
		print(colored("Error: can not put file in hdfs cluster. check file path properly" ,'red'))
		return False
	else:
		print(colored("file put successfully in clutser" ,'green'))
		return True

def hadoop():
	print(colored("Welcome to hadoop menu.." ,"yellow"))
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
			print(colored("Exit." ,"magenta"))
			exit()


def render(text,style):
	f=Figlet(font=style)
	print('\n'*1)
	print(f.renderText(text))
os.system("clear")
os.system("tput setaf 3")
render('ARTH TEAM TASK','epic')
os.system("tput setaf 7")

os.system("tput setaf 10")
render('\t by ARTH2020.1.17','digital')

os.system("tput setaf 2")
print("1. Enter MAIN MENU")
print("2. EXIT")
print("Enter Your Choice ", end=" : ")
x=input()

if int(x)==1:                                                                              #main menu
    while True:
        os.system("clear")
        os.system("tput setaf 10")
        render('                              MAIN MENU','bubble')
        os.system("tput setaf 33")
        print("""                 1. Docker Services
                 2. LVM Services
                 3. AWS Services
                 4. Hadoop Services
                 """)
        os.system("tput setaf 33")
        print("                 Enter Your Choice: ",end=" ")
        service=input()
        os.system("tput setaf 7")

        if int(service) == 1:
            while True:
                os.system("clear")
                os.system("tput setaf 2")
                render('DOCKER SERVICES','digital')
                os.system("tput setaf 33")
                print("""
                    Press 1: Enter Menu
                    Press 2: Back
                    """)
                print("Enter Your Choice: ",end=" ")
                ch1=input()
                os.system("tput setaf 7")

                if int(ch1)==1:
                    dockerconf()
                else:
                    break

        elif int(service) == 2:
            while True:
                os.system("clear")
                os.system("tput setaf 2")
                render('LOGICAL VOLUME MANAGER','digital')
                os.system("tput setaf 33")
                print("""
                    Press 1: Enter Menu
                    Press 2: Back
                    """)
                print("Enter Your Choice: ",end=" ")
                ch1=input()
                os.system("tput setaf 7")

                if int(ch1)==1:
                    lvmconf()
                else:
                    break

        elif int(service) == 3:
            while True:
                os.system("clear")
                os.system("tput setaf 2")
                render('AWS SERVICES','digital')
                os.system("tput setaf 33")
                print("""
                    Press 1: Enter Menu
                    Press 2: Back
                    """)
                print("Enter Your Choice: ",end=" ")
                ch1=input()
                os.system("tput setaf 7")

                if int(ch1)==1:
                    awsconf()
                else:
                    break

        elif int(service) == 4:
            while True:
                os.system("clear")
                os.system("tput setaf 2")
                render('HADOOP SERVICES','digital')
                os.system("tput setaf 33")
                print("""
                    Press 1: Enter Menu
                    Press 2: Back
                    """)
                print("Enter Your Choice: ",end=" ")
                ch1=input()
                os.system("tput setaf 7")

                if int(ch1)==1:
                    hadoop()
                else:
                    break

        else:
            break

        #ch=input("Wrong input... Do you want to continue(y/n): ")
        
    
else :
    os.system("clear")
    os.system("tput setaf 3")
    render('THANK YOU','epic')
    os.system("exit")
    os.system("tput setaf 7")

