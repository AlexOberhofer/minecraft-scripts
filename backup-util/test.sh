
#note backup will need to happen during server restart
for i in {1..5}
do
   echo "RUNNING BACKUP $i"
   python3 ./backup-world.py /mnt/f/Minecraft/world/
   echo "SLEEPING..."
   sleep 1m
done