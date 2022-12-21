from superannotate import SAClient
import os


def save_to_super_annotate(url, name):
    client = SAClient(
        token="a6b4814d75ba7ae2d02d7e2633545adff33d50acff43cf965537e2736758993644bffe050a5fb2b6t=14519"
    )
    return client.attach_items(
        project="obj_det",
        attachments=[
            {"name": name,
             "url": url},
        ],
        annotation_status="NotStarted"
    )


full_url = os.path.join(f'http://172.20.10.3:8080/static_files/Tigran_CV.png')


resp = save_to_super_annotate(url=full_url, name='cv4')




ls = ['war in ukrane', 'confict in the dobas', 'special operation of putin in south ukrane']

db = [set('war', 'in', 'ukrake')]
for i in ls:
    i = i.split()
    for j in i:
        db.append(set(j))





