from django.shortcuts import render, HttpResponse

from .models import Country
from cmp.forms import editCountryForm

from .models import Rank
from cmp.forms import editRankForm

from .models import Cemetery 
from cmp.forms import editCemeteryForm


def cemeteries(request):
    cemeteries = Cemetery.objects.all()
    return render(request, 'cmp/cemeteries.html', {'cemeteries': cemeteries})


def countries(request):
    countries = Country.objects.all()
    return render(request, 'cmp/countries.html', {'countries': countries})


def ranks(request):
    ranks = Rank.objects.all()
    return render(request, 'cmp/ranks.html', {'ranks': ranks})


def index(request):
    return render(request, "cmp/index.html")


def army_number_search(request):
    post = request.POST
    if post:
        try:
            army_number = int(post.get("q"))
        except ValueError:
            return HttpResponse("Please enter a valid Army Number")
        return original_unit(request, army_number)
    return render(request, "cmp/army-number-search.html")


def trigger_error(request):
    """error for Sentry"""
    division_by_zero = 1 / 0


def belongsTo(value: int, rangeStart: int, rangeEnd: int):
    if type(value) != int:
        return False
    elif value >= rangeStart and value <= rangeEnd:
        return True
    else:
        return False


def original_unit(request, army_number):
    army_number_index = {
        "Royal Army Service Corps (Block 1)": [1, 294000],
        "Royal Army Service Corps (Block 2)": [10660001, 11000000],
        "1st Life Guards": [294001, 299000],
        "2nd Life Guards": [299001, 304000],
        "Royal Horse Guards": [304001, 309000],
        # Cavalry of the Line 309001 - 721000 (Inclusive 558471 to 558761 allocated to the Royal Armoured Corps extraordinary to the block of numbers later allocated)
        "Lancers": [309001, 386000],
        "Dragoons": [386001, 528000],
        "Hussars": [528001, 721000],
        "Royal Artillery (Field, Coastal & Anti-Aircraft) 1": [721001, 1842000],
        "Royal Artillery (Field, Coastal & Anti-Aircraft) 2": [11000001, 11500000],
        "Royal Engineers": [1842001, 2303000],
        "Royal Corps of Signals": [2303001, 2604000],
        "Grenadier Guards": [2604001, 2646000],
        "Coldstream Guards": [2646001, 2688000],
        "Scots Guards": [2688001, 2714000],
        "Irish Guards": [2714001, 2730000],
        "Welsh Guards": [2730001, 2744000],
        "Black Watch (The Royal Highland Regiment)": [2744001, 2809000],
        "Seaforth Highlanders": [2809001, 2865000],
        "Gordon Highlanders": [2865001, 2921000],
        "Cameron Highlanders": [2921001, 2966000],
        "Argyll & Sutherland Highlanders": [2966001, 3044000],
        "Royal Scots": [3044001, 3122000],
        "Royal Scots Fusiliers": [3122001, 3178000],
        "The King's Own Scottish Borderers": [3178001, 3233000],
        "Cameronians (Scottish Rifles)": [3233001, 3299000],
        "Highland Light Infantry": [3299001, 3377000],
        "East Lancashire Regiment": [3377001, 3433000],
        "Lancashire Fusiliers": [3433001, 3511000],
        "Manchester Regiment": [3511001, 3589000],
        "Border Regiment": [3589001, 3644000],
        "The Prince of Wales Volunteers": [3644001, 3701000],
        "The King's Own Royal Regiment": [3701001, 3757000],
        "The King's Regiment": [3757001, 3846000],
        "The Loyal Regiment": [3846001, 3902000],
        "South Wales Borderers": [3902001, 3947000],
        "Welch Regiment": [3947001, 4025000],
        "The King's Shropshire Light Infantry": [4025001, 4070000],
        "Monmouthshire Regiment": [4070001, 4103000],
        "Herefordshire Regiment": [4103001, 4114000],
        "Cheshire Regiment": [4114001, 4178000],
        "Royal Welch Fusiliers": [4178001, 4256000],
        "Royal Northumberland Fusiliers": [4256001, 4334000],
        "East Yorkshire Regiment": [4334001, 4379000],
        "The Green Howards": [4379001, 4435000],
        "Durham Light Infantry": [4435001, 4523000],
        "West Yorkshire Regiment": [4523001, 4601000],
        "The Duke of Wellington's Regiment (The West Riding)": [4601001, 4680000],
        "The King's Own Yorkshire Light Infantry": [4680001, 4736000],
        "York & Lancaster Regiment": [4736001, 4792000],
        "Lincolnshire Regiment": [4792001, 4848000],
        "Leicestershire Regiment": [4848001, 4904000],
        "South Staffordshire Regiment": [4904001, 4960000],
        "Sherwood Foresters": [4960001, 5038000],
        "North Staffordshire Regiment": [5038001, 5094000],
        "Royal Warwickshire Regiment": [5094001, 5172000],
        "Gloucestershire Regiment": [5172001, 5239000],
        "Worcestershire Regiment": [5239001, 5328000],
        "Royal Berkshire Regiment": [5328001, 5373000],
        "Oxfordshire & Buckinghamshire Light Infantry": [5373001, 5429000],
        "The Duke of Cornwall's Light Infantry": [5429001, 5485000],
        "Hampshire Regiment": [5485001, 5562000],
        "Wiltshire Regiment": [5562001, 5608000],
        "Devonshire Regiment": [5608001, 5662000],
        "Somerset Light Infantry": [5662001, 5718000],
        "Dorsetshire Regiment": [5718001, 5763000],
        "Royal Norfolk Regiment": [5763001, 5819000],
        "Suffolk Regiment": [5819001, 5875000],
        "Northamptonshire Regiment": [5875001, 5931000],
        "Cambridgeshire Regiment": [5931001, 5942000],
        "Bedfordshire & Hertfordshire Regiment": [5942001, 5998000],
        "Essex Regiment": [5998001, 6076000],
        "The Queen's Royal Regiment": [6076001, 6132000],
        "East Surrey Regiment": [6132001, 6188000],
        "Middlesex Regiment": [6188001, 6278000],
        "The Buffs (East Kent Regiment)": [6278001, 6334000],
        "Royal West Kent Regiment": [6334001, 6390000],
        "Royal Sussex Regiment": [6390001, 6446000],
        "Royal Fusiliers": [6446001, 6515000],
        "London Regiment": [6515001, 6802500],
        "The Inns of Court Regiment": [6802501, 6814000],
        "Honourable Artillery Company (Infantry)": [6825001, 6837000],
        "The King's Royal Rifle Corps": [6837001, 6905000],
        "The Rifle Brigade": [6905001, 6972000],
        "Royal Inniskilling Fusiliers": [6972001, 7006000],
        "Royal Ulster Rifles": [7006001, 7040000],
        "Royal Irish Fusiliers": [7040001, 7075000],
        "Royal Dublin Fusiliers (Disbanded 1922)": [7075001, 7109000],
        "Royal Irish Regiment": [7109001, 7143000],
        "Connaught Rangers (Disbanded 1922)": [7143001, 7177000],
        "Leinster Regiment (Disbanded 1922)": [7177001, 7211000],
        "Royal Munster Fusiliers (Disbanded 1922)": [7211001, 7245000],
        "Royal Army Medical Corps": [7245001, 7536000],
        "(Royal) Army Dental Corps (Block 1)": [7536001, 7539000],
        "(Royal) Army Dental Corps (Block 2)": [10510001, 10530000],
        "Royal Guernsey Militia and Royal Alderney Artillery Militia (Discontinued 1929)": [
            7539001,
            7560000,
        ],
        "Royal Militia of the Island of Jersey (Discontinued 1929)": [7560001, 7574000],
        "Royal Army Ordnance Corps (Block 1)": [7574001, 7657000],
        "Royal Army Ordnance Corps (Block 2)": [10530001, 10600000],
        "(Royal) Army Pay Corps (Block 1)": [7657001, 7681000],
        "(Royal) Army Pay Corps (Block 2)": [10400001, 10500000],
        "(Locally enlisted staff Middle East)": [10500001, 10508000],
        "(Royal) Military Police": [7681001, 7717000],
        "Military Provost Staff Corps": [7717001, 7718800],
        "Small Arms School Corps": [7718801, 7720400],
        "(Royal) Army Education Corps": [7720401, 7732400],
        "Band of the Royal Military College": [7732401, 7733000],
        "Corps of Military Accountants (Disbanded 1925)": [7733001, 7757000],
        "Royal Army Veterinary Corps": [7757001, 7807000],
        "Machine Gun Corps (Disbanded 1922)": [7807001, 7868000],
        "Royal Tank Regiment": [7868001, 7891868],
        "Royal Armoured Corps (Block 1)": [7891869, 8230000],
        "Royal Armoured Corps (Block 2)": [558471, 558761],
        #'Militia 10000000 - 10350000 (Army Numbers were allocated in accordance with Regulations for the Militia [Other than the Supplementary Reserve], 1939, paras. 11-13)
        "Intelligence Corps": [10350001, 10400000],
        "Reconnaissance Corps": [10600001, 10630000],
        "Army Catering Corps": [10630001, 10655000],
        "Army Physical Training (Staff) Corps": [10655001, 10660000],
        "(Royal) Pioneer Corps": [13000001, 14000000],
        "The Lowland Regiment": [14000001, 14002500],
        "The Highland Regiment": [14002501, 14005000],
        "General Service Corps": [14200001, 15000000],
        "Indian local enlistments": [15000001, 15005000],
        "Royal Electrical & Mechanical Engineers": [16000001, 16100000],
        "Non-Combatant Corps": [97000001, 97100000],
        # Auxiliary Territorial Service W/1 - W/500,000
        # Voluntary Aid Detachments W/500001 - W/1000000
        # Post War Numbering system.
        "Until October 1950": [22000000, 22199408],
        "November 1950 until February 1951": [22199409, 22460786],
        "February 1951 until July 1951": [22460787, 22562759],
        "July 1951 until June 1955": [22562760, 23052500],
        "June 1955 until October 1955": [23052501, 23188252],
        "October 1955 until May 1956": [23188253, 23479123],
        "May 1956 until October 1960": [23479124, 23845071],
        "October 1960 until April 1964": [23845072, 23969619],
        "April 1964 until October 1964": [23969620, 24033484],
        "Until April 1965": [24033485, 24057159],
        "Until December 1966": [24057160, 24076468],
        "Until April 1969": [24076469, 24182226],
        "Until September 1971": [24182227, 24262662],
        "Until September 1972": [24262663, 24302033],
        "Until January 1973": [24302034, 24315610],
        "Until February 1973": [24315611, 24322198],
        "Until August 1974": [24322199, 24355527],
        "Until September 1975": [24355528, 24369281],
        "Until May 1978": [24369282, 24475540],
        "Until March 1979": [24475541, 24520161],
        "Until August 1980": [24520162, 24579860],
        "Until December 1985": [24587119, 24753060],
        "Until November 1988": [24753061, 24854044],
        "Until January 1992": [24854045, 25012465],
        "January 1992 to July 1993": [25012466, 25027818],
        "July 1993 to August 1995": [25027819, 25041250],
        "August 1995 to July 1997": [25041251, 25065603],
        "January 1998 to January 1999": [25073583, 25087140],
        "January 1999 to September 2000": [25087141, 25122315],
        "September 2000 to April 2001": [25122316, 25112186],
        "August 2001 to July 2003": [25136866, 25139703],
        "Jul 2003 to Sep 2003 ": [25170931, 25177141],
        "Oct 2003 to Jun 2004 ": [25177142, 25189124],
    }
    for unit in army_number_index:
        # Uncomment this breakpoint to work with ipdb:
        # breakpoint()
        # embed()
        original_unit = belongsTo(
            army_number, army_number_index[unit][0], army_number_index[unit][1]
        )
        if original_unit is True:
            return HttpResponse(unit)
    return HttpResponse("No Match Found")


def edit_cemeteries(request):
    post = request.POST
    form = editCemeteryForm(post or None)
    if post and form.is_valid():
        form.save()
        return HttpResponse("Cemetery Added")
    return render(request, "cmp/edit-cemeteries.html", {"form": form})


def edit_countries(request):
    post = request.POST
    form = editCountryForm(post or None)
    if post and form.is_valid():
        form.save()
        return HttpResponse("Country Added")
    return render(request, "cmp/edit-countries.html", {"form": form})


def edit_ranks(request):
    post = request.POST
    form = editRankForm(post or None)
    if post and form.is_valid():
        form.save()
        return HttpResponse("Rank Added")
    return render(request, "cmp/edit-ranks.html", {"form": form})