import sys
import manage

firstrun = "runserver" not in sys.argv
if firstrun:
    sys.argv.insert(1, "runserver")
print(sys.argv)

manage.main()
