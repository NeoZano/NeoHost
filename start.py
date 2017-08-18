from server import run_server
from sys import argv as args



def main():
  args.pop(0)
  ip_def = False
  port_def = False
  for arg in range(len(args)):
    if args[arg] == "-p":
      port = args[arg+1]
      port_def = True
    elif args[arg] == "-i":
      ip = args[arg+1]
      ip_def = True
  if ip_def == True and port_def == True:
    run_server(ip,int(port))
  elif ip_def == True:
    run_server(ip)
  elif port_def == True:
    run_server('127.0.0.1',int(port))
  else:
    run_server()
main()