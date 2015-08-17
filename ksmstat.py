#!/usr/bin/python
#-shkbuilder
import sys,subprocess
if len(sys.argv) > 1:
  print "----------------------------------------------------------------------------"
  print "http://www.kernel.org/doc/Documentation/vm/ksm.txt :"
  print "\n" 
  print "The effectiveness of KSM and MADV_MERGEABLE is shown in /sys/kernel/mm/ksm/:"
  print "\n" 
  print "pages_shared - how many shared pages are being used"
  print "pages_sharing - how many more sites are sharing them i.e. how much saved"
  print "pages_unshared - how many pages unique but repeatedly checked for merging"
  print "pages_volatile - how many pages changing too fast to be placed in a tree"
  print "full_scans - how many times all mergeable areas have been scanned"
  print "\n" 
  print "A high ratio of pages_sharing to pages_shared indicates good sharing, but"
  print "a high ratio of pages_unshared to pages_sharing indicates wasted effort."
  print "pages_volatile embraces several different kinds of activity, but a high"
  print "proportion there would also indicate poor use of madvise MADV_MERGEABLE."
  print "----------------------------------------------------------------------------"
  print "\n"

print "KSM Stats:"
#print(float(open("/sys/kernel/mm/ksm/pages_shared","r").readline().strip())/float(open("/sys/kernel/mm/ksm/pages_sharing","r").readline().strip()))'
pages_shared = float(open("/sys/kernel/mm/ksm/pages_shared","r").readline().strip())
pages_sharing = float(open("/sys/kernel/mm/ksm/pages_sharing","r").readline().strip())
pages_unshared = float(open("/sys/kernel/mm/ksm/pages_unshared","r").readline().strip())
sp = subprocess.Popen(['getconf', 'PAGESIZE'], shell=False, stdout=subprocess.PIPE)
sp2 = subprocess.Popen(['/etc/init.d/ksmtuned', 'status'], shell=False, stdout=subprocess.PIPE)
output = float(sp.stdout.read().strip())
#output = float(subprocess.check_output(["getconf", "PAGESIZE"]).strip())
outputt = sp2.stdout.read()
print outputt
print "Pagesize:", output
print "Shared total:", output * pages_shared
print "KSM efficiency:", pages_sharing / pages_shared
print "Wasted effort:", pages_unshared / pages_sharing
