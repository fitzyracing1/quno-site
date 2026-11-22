from PIL import Image, ImageDraw, ImageFont
W,H=1200,630
img=Image.new("RGB",(W,H),(11,15,25))
d=ImageDraw.Draw(img)
# subtle grid
for x in range(0,W,40): d.line([(x,0),(x,H)],fill=(17,23,37))
for y in range(0,H,40): d.line([(0,y),(W,y)],fill=(17,23,37))
d.rectangle([0,0,14,H],fill=(0,82,255))
def F(w,s):
    f=ImageFont.truetype("/usr/share/fonts/truetype/sand-box/google/Inter/Inter-VariableFont_opsz,wght.ttf",s)
    try: f.set_variation_by_axes([32 if s>40 else 14, w])
    except Exception: pass
    return f
mono=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",30)
d.text((80,70),"Quno",font=F(800,120),fill=(255,255,255))
d.text((80,225),"Official and on-chain data for bots,",font=F(600,50),fill=(230,236,248))
d.text((80,288),"paid per call over x402 (USDC on Base).",font=F(600,50),fill=(230,236,248))
items=["Base token risk  $0.02","x402 market data  $0.01","Weather by ZIP  $0.004","NASA space weather  $0.005"]
x,y=80,395
for i,t in enumerate(items):
    bx=x+(i%2)*530; by=y+(i//2)*70
    d.rounded_rectangle([bx,by,bx+500,by+54],radius=12,fill=(20,28,46),outline=(0,82,255),width=2)
    d.text((bx+22,by+11),t,font=F(600,28),fill=(255,255,255))
d.text((80,560),"GET a route  ->  HTTP 402  ->  pay USDC  ->  200 JSON",font=mono,fill=(120,160,255))
img.save("og.png",optimize=True)
print(img.size)
