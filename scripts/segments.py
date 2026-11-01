# Same segmentation as bank/finish_item.sh: 1400-frame segments, tail <400 frames merged into the last.
import json, sys
tot = json.load(open(sys.argv[1]))['total']; SEG = int(sys.argv[2]) if len(sys.argv) > 2 else 1400
only = sys.argv[3].split(',') if len(sys.argv) > 3 and sys.argv[3] else None
out = []; pos = 0
while pos < tot:
    a = pos; b = a + SEG - 1
    if tot - b < 400: b = tot - 1
    if b >= tot: b = tot - 1
    tag = 's%06d' % a
    if not only or tag in only: out.append({'tag': tag, 'a': a, 'b': b})
    pos = b + 1
print(json.dumps(out))
