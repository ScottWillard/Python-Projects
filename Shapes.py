import Twister as Twister
import math

def displacement(x, width, wrapping_angle):
    """
       Function for converting a nanosheet coordinate into a partly wrapped nanotube
       @param x : Coordinates of nanosheet atom
       @param width : Width of the nano-sheet
       @param wrapping_angle : maximum wrapping angle of the nanotube in radians
    """
    # calculate the average radius of the incomplete wrapped tube
    radius = width/wrapping_angle
    # find the angle of the current atom
    angle = (x[2]-width/2.)/radius
    # calculate the radius of the current atom
    atom_radius = radius+x[1]

    # return atom position of the wrapped atom
    return numpy.array([x[0], atom_radius*math.cos(angle),atom_radius*math.sin(angle)])

def configuration(n, m, repetition):
    """
       Function for generating a moebius molecule
       @param n : Chiral vector index
       @param m : Chiral vector index
       @param repetition : Repetition along z
    """

    # build n,m ribbon
    ribbon = NanoRibbon(n,m)
    ribbon = ribbon.repeat(1,1,repetition)

    # get properties of the ribbon
    lattice = ribbon.bravaisLattice()
    elements = ribbon.elements()
    cartesian_coordinates=ribbon.cartesianCoordinates().inUnitsOf(Angstrom)

    # calculate the length of the 1-d structure
    z_length = numpy.linalg.norm(lattice.primitiveVectors()[2].inUnitsOf(Angstrom))

    # calculate twist parameters
    rotation_angle_per_z =  math.pi /z_length
    rotation_axis = numpy.array([0,0,1])
    rotation_axis_center = numpy.sum(cartesian_coordinates,axis=0)/len(cartesian_coordinates)

    # define a function of one variable, f(c),  for displacing the atoms
    f = lambda c : Twister.displacement(c, rotation_angle_per_z, rotation_axis,
                                rotation_axis_center, 0.,z_length)
    # apply the function to find new displaced coordinates
    cartesian_coordinates = numpy.apply_along_axis(f, 1, cartesian_coordinates)
    cartesian_center = numpy.sum(cartesian_coordinates,axis=0)/len(cartesian_coordinates)
    cartesian_coordinates = cartesian_coordinates - cartesian_center


    # define a function of one variable, f(c),  for displacing the atoms
    f = lambda c : displacement(c, z_length,2.0*math.pi)
    # apply the function to find new displaced coordinates
    cartesian_coordinates = numpy.apply_along_axis(f, 1, cartesian_coordinates)

    return MoleculeConfiguration(
            elements=elements,
            cartesian_coordinates=cartesian_coordinates * Angstrom
            )

# Instantiate the builder object and choose our title
builder = Builder()
builder.title('Moebius ribbon')

# Set the configuration generator
builder.setConfigurationGenerator(configuration)

# Tube properties group
builder.newGroup('Tube parameters')
builder.integer( 'n', 6, 'n', min=1, max=1000)
builder.integer( 'm', 0, 'm', min=0, max=1000)
builder.integer( 'repetition', 40, 'C-direction', min=1, max=1000)