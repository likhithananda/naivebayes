import os
import sys
import re
import math
final_dataTest=[]
dictionaryArrays=[]
def getFiles(path):
	array1=[]
	Sum=0
	value=0
	d={}
	for filename in os.scandir(path):
		if filename.is_file():
			count=0
			f=open(filename,'r')
			for row in f:
				beg=0
				end=0
				count=count+1
				if row.find("Lines:")>-1:
					beg=count
					#print("beg:",beg)
					array1=int(row.split("Lines:")[1])
					end=beg+array1
					#print("end:",end)
					CleanData(f,beg,end,d)
	#od=collections.OrderedDict(sorted(d.items()))
	for key in d:
		value=d.get(key,1)
		Sum= Sum+int(value)
	#print(value,"Value")
	#print("Sum",Sum)
	return d,Sum
			
def CleanData(f,beg,end,d):
	for index, line in enumerate(f):
		if 0 <= index <= end:
			line = re.sub(r"[^a-zA-Z0-9]+"," ",line.lower())
			if(line != " "):
				nostop(line,d)
	return d
	
def nostop(line,d):
	stopwords = ["","a","about","above","after","again","against","all","am","an","and", "any","are","aren't","as","at","be","because","been","before","being",
        "below","between","both","but","by","can't","cannot","could","couldn't","did","didn't","do","does","doesn't","doing","don't","down",
        "during","each","few","for","from","further","had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","he's","her","here",
        "here's","hers","herself","him","himself","his","how","how's","i","i'd","i'll","i'm","i've","if","in","into","is","isn't","it","it's", "its",
        "itself","let's","me","more","most","mustn't","my","myself","no","nor","not", "of","off","on","once","only","or","other","ought","our","ours",
        "ourselves","out","over","own","same","shan't","she","she'd","she'll","she's","should","shouldn't","so","shall","some","such","than","that",
        "that's","the","their","theirs","them","themselves","then","there","there's","these","they","they'd","they'll","they're","they've","this","those",
        "through","to","too","under","until","up","very","was","wasn't","we","we'd","we'll","we're","we've","were","weren't","what","what's","when",
        "when's","where","where's","which","while","who","who's","whose","whom","why","why's","with","won't","would","wouldn't","you","you'd","you'll",
        "you're","you've","your","yours","yourself","yourselves"]
	l={}
	final_data=[]
	token=[]
	token=line.split(" ")
	for p in token:
		if p not in stopwords:
			final_data.append(p)
	#print("final_data",final_data)
	
	for y in final_data:
		if y not in l:
			l[y]=1
		else:
			l[y]+=1
	for h in l:
		if h not in d:
			d[h]=l[h]
		else:
			d[h]+=l[h]
	return(d)

def getFiles_test(pth,dictionaryArrays,ind,Sum_Arr,prior_array):
	#print("in test")
	array1test=[]
	correct=0
	wrong=0

	for filename in os.scandir(pth):
		#print("for class in test")
		if filename.is_file():
			#print("for one file")
			FinalTestToken=[]
			count=0
			fTest=open(filename,'r')
			for row in fTest:
				begTest=0
				endTest=0
				count=count+1
				if row.find("Lines:")>-1:
					begTest=count
					#print("beg:",beg)
					array1test=int(row.split("Lines:")[1])
					endTest=begTest+array1test
					#print("end:",end)
					CleanDataTest(fTest,begTest,endTest,FinalTestToken)
		#print("for each file",FinalTestToken)
		correct,wrong=conditional_probs(FinalTestToken,dictionaryArrays,ind,Sum_Arr,prior_array,correct,wrong)
	#print ("correct",correct)
	#print ("wrong",wrong)
	print("accuracy of",pth,(correct/(correct+wrong))*100)
	return correct,wrong

def conditional_probs(FinalTestToken,dictionaryArrays,ind,Sum_Arr,prior_array,correct,wrong):
	#print("for each file in one class")
	likelihood=0.0
	posterior_array=[]
	for j in range(len(dictionaryArrays)):
		#print("loop",j)
		loglik=0
		for word in FinalTestToken:
			#print("word",word)
			value=dictionaryArrays[j].get(word,0)
			#print("value",value)
			likelihood=(value+1)/(Sum_Arr[j]+len(dictionaryArrays[j]))
			loglik+=math.log(likelihood)
			#print("log likelihood",loglik)
		posterior=loglik+math.log(prior_array[j])
		#print("posterior",posterior)
		posterior_array.append(posterior)
	#print("array post",posterior_array)
	pred_ind=posterior_array.index(max(posterior_array))
	return accuracy(ind, pred_ind,correct,wrong)

	
def accuracy(ind, pred_ind,correct,wrong):
	if (ind==pred_ind):
		correct+=1
	else:
		wrong+=1
	return correct,wrong

def CleanDataTest(fTest,begTest,endTest,FinalTestToken):
	final_dataTest=[]
	for index, line in enumerate(fTest):
		if 0 <= index <= endTest:
			line = re.sub(r"[^a-zA-Z0-9]+"," ",line.lower())
			if(line != " "):
				nostopTest(line,FinalTestToken)
			

def nostopTest(line,FinalTestToken):
	stopwords = ["","a","about","above","after","again","against","all","am","an","and", "any","are","aren't","as","at","be","because","been","before","being",
        "below","between","both","but","by","can't","cannot","could","couldn't","did","didn't","do","does","doesn't","doing","don't","down",
        "during","each","few","for","from","further","had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","he's","her","here",
        "here's","hers","herself","him","himself","his","how","how's","i","i'd","i'll","i'm","i've","if","in","into","is","isn't","it","it's", "its",
        "itself","let's","me","more","most","mustn't","my","myself","no","nor","not", "of","off","on","once","only","or","other","ought","our","ours",
        "ourselves","out","over","own","same","shan't","she","she'd","she'll","she's","should","shouldn't","so","shall","some","such","than","that",
        "that's","the","their","theirs","them","themselves","then","there","there's","these","they","they'd","they'll","they're","they've","this","those",
        "through","to","too","under","until","up","very","was","wasn't","we","we'd","we'll","we're","we've","were","weren't","what","what's","when",
        "when's","where","where's","which","while","who","who's","whose","whom","why","why's","with","won't","would","wouldn't","you","you'd","you'll",
        "you're","you've","your","yours","yourself","yourselves"]
	
	finalDataTest=[]
	token_dataTest=[]
	token=[]
	token=line.split(" ")
	for p in token:
		if p not in stopwords:
			token_dataTest.append(p)
	#print("Test Tokens each line",token_dataTest)
	for e in token_dataTest:
		FinalTestToken.append(e)
		
def prior(Sum_Arr):
	total=0
	priors=[]
	for i in range(len(Sum_Arr)):
			total+=Sum_Arr[i]
	#print("total",total)
	for i in range(len(Sum_Arr)):
		prior=Sum_Arr[i]/total
		priors.append(prior)
	#print("priors",priors)
	return priors	
	
def main(args):
	Sum_Arr=[]
	#print("for training Data")
	train=[f for f in os.listdir(args[1])]
	#print(train)
	dictionaryArrays=[]
	for f in train:
		#print("for each train")
		#d1={}
		pathTrain=args[1]+"\\"+f
		#print("p",pathTrain)
		#print("For each class")
		d1,Sum=getFiles(pathTrain)
		Sum_Arr.append(Sum)
		#print("sum array",Sum_Arr)
		dictionaryArrays.append(d1) #here calculate the length of dictinonaries
		prior_array=prior(Sum_Arr)
	#print("For Test Data")
	test=[h for h in os.listdir(args[2])]
	#print(test)
	ind=0
	c=0
	w=0
	for r in test:
		tok1=[]
		#print("for each test")
		pathTest=args[2]+"\\"+r
		#print("path Test",pathTest)
		correct,wrong=getFiles_test(pathTest,dictionaryArrays,ind,Sum_Arr,prior_array)
		c+=correct
		w+=wrong
		ind+=1
	
	print("total accuracy",(c/(c+w))*100)
	#print("dictionary arrays",dictionaryArrays)
	#print("for Test data")
	#test1='temptest\\alt.atheism'
	#print("for test1")
	#tok1=getFiles_test(test1)
	
main(sys.argv)