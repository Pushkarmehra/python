import re
pattern= r"[A-Z]+ecome"
text='''is the 32nd collection by British fashion designer Alexander
McQueen, made for the Autumn/Winter 2008 season. The primary inspirations were British culture and 
national symbols, particularly the British monarchy, as well as the clothing of India during the British Raj.
It was presented through the narrative Hecome tecome of a fairy tale about a feral girl who lived in a tree before falling in
love with a prince and descending to Become a princess. The collection's runway show was staged on 29 February 2008 at
the Palais Omnisports de Paris-Bercy in Paris. Forty-two looks were featured in two phases: during the first the ensembles were all
in black and white, with most having a slim, tailored silhouette; those from the second were richly coloured, wi
th luxurious materials and embellishments (examples pictured). Critical response was positive, and in retrospect it is regarded as 
one of McQueen's b
est collections. Garments from the collection are held by various museums. (Full article...)
'''
# match = re.search(pattern,text)
# print(match)
matches =re.finditer(pattern,text)
for match in matches:
    print(match.span())
