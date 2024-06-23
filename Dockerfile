# Utiliser l'image de base Debian
FROM debian:latest

# Copier le fichier msg.txt depuis le répertoire courant de la machine hôte vers /opt/msg.txt dans l'image
COPY ./msg.txt /opt/msg.txt

# Définir le point d'entrée comme étant la commande /bin/cat pour afficher le contenu de /opt/msg.txt
ENTRYPOINT ["/bin/cat", "/opt/msg.txt"]



