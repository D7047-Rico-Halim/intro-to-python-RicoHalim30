from main import VolumeBalok, VolumeKubus

def test_volume_balok():
    assert VolumeBalok(2, 3, 4) == 24
    assert VolumeBalok(5, 6, 7) == 210
    assert VolumeBalok(8, 9, 10) == 720
    
def test_volume_kubus():
    assert VolumeKubus(2) == 8
    assert VolumeKubus(3) == 27
    assert VolumeKubus(4) == 64