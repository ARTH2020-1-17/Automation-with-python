#!/usr/bin/python3

import os
import subprocess as sp
from hadoop import *

def MENU():
    print('Services - ')
    print('1. Docker')
    print('2. LVM')
    print('3. AWS')
    print('4. Hadoop')
    service = int(input('Enter here : '))
    if service == 1:
        dockerconf()
    elif service == 2:
        lvmconf()
    elif service == 3:
        awsconf()
    elif service == 4:
        hadoop()
    else : 
        print('unsupported input')
        

def dockerconf():
    ec = sp.getoutput('docker --version | echo $?')
    if ec != 0 :
        print('docker is not installed')
        pass
    else :
        print("-----------DOCKER-----------")
        print("1. Docker daemon start/stop/status")
        print("2. Show docker process")
        print("3. Show docker images")
        print("4. Search images on docker hub")
        print("5. Download docker image from docker hub")
        print("6. Run a docker image")
        print("7. Stop docker container")
        print("8. Delete docker image")
        print("9. Configure webserver(httpd) in docker container")
        command = input('\nEnter your choice - ')
        if command == 1:
            op = input('1.start  2.stop  3.status')
            if op == 1: sp.getoutput('systemctl start docker')
            elif op == 2: sp.getoutput('sytemctl stop docker')
            elif op == 3: sp.getoutput('systemctl status docker')
            else: print('unsupported input')
        elif command == 2:
            op = input('1.Recent process  2.All process')
            if op == 1: sp.getoutput('docker ps')
            elif op == 2: sp.getoutput('docker ps -a')
            else: print('unsupported input')
        elif command == 3: sp.getoutput('docker images')
        elif command == 4:
            im = input('image name - ')
            sp.getoutput('docker search {}'.format(im))
        elif command == 5:
            im = input('image name - ')
            sp.getoutput('docker pull {}'.format(im))
        elif command == 6:
            im = input('image name - ')
            sp.getoutput('docker run -it {} &'.format(im))
        elif command == 7:
            im = input('image name - ')
            sp.getoutput('docker stop {}'.format(im))
        elif command == 8:
            im = input('image name - ')
            sp.getoutput('docker rmi {}'.format(im))
        elif command == 9:
            httpdconf()
        else: print('Error')
        
        
#def httpdconf()        
#def Menussh()
def lvmconf():

	print("\t\t--------LVM Partitions-------")
	print("1. Check available disks")
	print("2. Create physical volumes(PV)")
	print("3. Create Volume Group (VG)")
	print("4. Create Logical volumes(LV)")
	print("5. Format the created LV")
	print("6. Mount the LV")
	print("7. Extend Volume Group")
	print("8. Format the extende volume")
	print("9. To display volume group.")
	print("0. to display Logical volume.")
	lvm = int(input("Enter your choice : "))
	if lvm == 1:
		p = os.system('fdisk -l')
		print(p)
	elif lvm == 2:
		def pv():
			vol = input("Enter name of disk : ")
			q = os.system('pvcreate {0}'.format(vol))
			print(q)			
		x=input("Do you want to convert harddisk into physical volume (y/n):")
		if (x == "y") or (x == "Y"):
			pv()
		else:
			lvmconf()
	
	elif lvm == 3:
		a = input("Enter the name for volume group :")
		b = input("Enter name of physical volume:")
		c = input("Enter name of physical volume:")
		s = os.system("vgcreate {0} {1} {2}".format(a,b,c))
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
	elif lvm == 7:
		u = input("Howm much size do you want to extend ,Enter size in (G/M/T):")
		w = input("Enter name of created volume group: ")
		v = input("Enter name of created LV :")
		resize = os.system("lvextend --size +{0}/{1}/{2}".format(u,w,v))
		print(resize)
	elif lvm == 8:
		r_v = input("Enter name of created volume group: ")
		r_l = input("Enter name of created LV :")
		re_frmt = os.system("resize2fs /dev/{0}/{1}".format(r_v,r_l))
		print(re_frmt)
	elif lvm == 9:
		vgname=input("enter vg name:")
		v_disp = os.system("vgdisplay {0}".format(vgname))
		print(v_disp)
	elif lvm == 0:
		vgname2=input("Entyer vg name:")
		lvname=input("Enter lv name:")
		lv_display=os.system("lvdisplay {}/{}".format(vgname2,lvname))
		print(lv_display)
	else:
		print("invalid input chech once again.")

def awsconf():
        print('--Services--')
        print('EC2')
        print('EBS')
        print('S3 ')
        aws_ser = input('Enter here : ')
        if aws_ser == 'EC2' or 'ec2' :
        	ec2conf()
        elif aws_ser == 'EBS' or 'ebs':
                ebsconf()
        elif aws_ser == 'S3' or 's3':
                s3conf()
        else :
                print('unsupported input')

def ec2conf():
    print("-----------EC2----------")
    print("1. Create/Delete Key Pair")
    print("2. Create/Delete Security group")
    print("3. EC2 instance start/stop/terminate")
    print("4. Show all instances ")
    print("5. Create new Instance")
    command = int(input('\nEnter your choice - '))
    if command ==1:
        kp = int(input('1.Create  2.Delete '))
        if kp == 1:
            key_name = input("Enter key name : ")
            sp.getoutput('aws ec2 create-key-pair --key-name {0}'.format(key_name))
        elif kp == 2:
            key_name = input("Enter key name : ")
            sp.getoutput('aws ec2 delete-key-pair --key-name {0}'.format(key_name))
        else :
            print('unsupported input')
    elif command ==2:
        sg = int(input('1.Create  2.Delete '))
        if sg == 1:
            se_group_name = input("Enter name for security group : ")
            se_disc = input("Enter description for security group : ")
            sp.getoutput('aws ec2 create-security-group --group-name {0} --description {1}'.format(se_group_name, se_disc))
        elif sg == 2:
            se_grp_id = input("Enter id of security group :")
            sp.getoutput('aws ec2 delete-security-group --group-id{0}'.format(se_grp_id))
        else : 
            print('unsupported input')
    elif command == 3:
        ins_id = input(" Enter Instance ID : ")
        op = int(input('1.start  2.stop  3.terminate'))
        if op == 1: 
            sp.getoutput('aws ec2 start-instances --instance-ids {0}'.format(ins_id))
        elif op == 2: 
            sp.getoutput('aws ec2 stop-instances --instance-ids {0}'.format(ins_id))
        elif op == 3: 
            sp.getoutput('aws ec2 terminate-instances --instance-ids {0}'.format(ins_id))
        else: 
            print('unsupported input')
    elif command == 4:
        l= sp.getoutput('aws ec2 describe-instances')
        print(l)
    elif command == 5:
        img_id = input("Enter image id : ")
        img_type = input("Enter image type : ")
        subnet_id = input("Enter subnetId : ")
        se_id = input("Enter security group id : ")
        key_name = input("Enter created  key name : ")
        sp.getoutput('aws ec2 run-instances --image-id {0} --instance-type {1} --subnet-id {2} --security-group-id {3} --key-name {4}'.format(
                img_id, img_type, subnet_id, se_id, key_name))
    else : 
        print('unsupported input')

def ebsconf():
    print("-----------EBS----------")
    print("1. Create EBS volume")
    print("2. Attach EBS volume to EC2 instance")
    command = int(input('\nEnter your choice - '))
    if command ==1:
        vt = input("Enter the type of volume : ")
        size = input("Enter the size of volume :")
        zone = input("Enter the name of avaiability zone :")
        sp.getoutput('aws ec2 create-volume --volume-type {0} --size {1}  --availability-zone {2}'.format(vt, size, zone))
    elif command ==2:
        vol_id = input("Enter volume id: ")
        instance_id = input("Enter instance id : ")
        dev_name = input("Enter device name or drive name : ")
        sp.getoutput('aws ec2 attach-volume --volume-id {0} --instance-id {1} --device {2}'.format(vol_id, instance_id, dev_name))
    else : 
        print('unsupported input')
            
            
def s3conf():
    print("-----------S3----------")
    print("1. Create Bucket")
    print("2. List buckets and objects")
    print("3. Create Object")
    print("4. Delete Bucket")
    print("5. Delete Object")
    command = int(input('\nEnter your choice - '))
    if command ==1:
        buck_name = input("Enter unique bucket name : ")
        s = sp.getoutput('aws s3 mb s3://{}'.format(buck_name))
        print(s)
    elif command ==2 :
        s = sp.getoutput('aws s3 ls')
        print(s)
    elif command ==3 :
        s = sp.getoutput('aws s3 sync')
        print(s)
    elif command ==4 :
        buck_name = input("Enter bucket name : ")
        s = sp.getoutput('aws s3 rb s3://{}'.format(buck_name))
        print(s)
    elif command ==5 :
        buck_name = input("Enter bucket name : ")
        obj_name = input("Enter object name : ")
        s = sp.getoutput('aws s3 rm s3://{0}/{1}'.format(buck_name,obj_name))
        print(s)
#def hadoopconf()

while(True):
    system = input('Do you want to use local or remote(l/r) - \n')
    if system == 'l':
        MENU()
    elif system == 'r':
        Menussh()
    else:
        print('unsupported input\n')
    x=input('Do you want to exit (y/n) - \n')
    if x == 'y':
        exit()

