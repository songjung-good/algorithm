def preorder(root):
    global pre
    pre.append(root)
    if ch_l[root] == 0 and ch_r[root] == 0:
        return
    else:
        if ch_l[root] != 0:
            preorder(ch_l[root])
        if ch_r[root] != 0:
            preorder(ch_r[root])


def inorder(root):
    global inr

    if ch_l[root] == 0 and ch_r[root] == 0:
        inr.append(root)
        return

    else:
        if ch_l[root] != 0:
            inorder(ch_l[root])
        inr.append(root)
        if ch_r[root] != 0:
            inorder(ch_r[root])


def postorder(root):
    global post

    if ch_l[root] == 0 and ch_r[root] == 0:
        post.append(root)
        return

    else:
        if ch_l[root] != 0:
            postorder(ch_l[root])
        if ch_r[root] != 0:
            postorder(ch_r[root])
        post.append(root)


N = int(input())
P = [0] * 27
ch_l = [0] * 27
ch_r = [0] * 27
for _ in range(N):
    p, l, r = input().split()
    p = ord(p) - 64

    if l != '.':
        l = ord(l) - 64
        P[l] = p
        ch_l[p] = l
    if r != '.':
        r = ord(r) - 64
        P[r] = p
        ch_r[p] = r

pre = []
inr = []
post = []

preorder(1), inorder(1), postorder(1)

ans_pre = ''
for pr in pre:
    ans_pre += chr(pr + 64)
print(ans_pre)

ans_inr = ''
for ir in inr:
    ans_inr += chr(ir + 64)
print(ans_inr)

ans_post = ''
for po in post:
    ans_post += chr(po + 64)
print(ans_post)