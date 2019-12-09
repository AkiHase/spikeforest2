import random
import hither

@hither.function('spykingcircus', '0.8.6-w1')
@hither.output_file('sorting_out')
@hither.container(default='docker://magland/sf-spykingcircus:0.8.6')
@hither.local_module('../../../spikeforest2_utils')
def spykingcircus(recording_path, sorting_out):
    import spiketoolkit as st
    import spikesorters as ss
    from spikeforest2_utils import AutoRecordingExtractor, AutoSortingExtractor

    recording = AutoRecordingExtractor(dict(path=recording_path), download=True)
    
    # Sorting
    print('Sorting...')
    sorter = ss.SpykingcircusSorter(
        recording=recording,
        output_folder='/tmp/tmp_spykingcircus_' + _random_string(8),
        delete_output_folder=True
    )

    sorter.set_params(
    )     
    timer = sorter.run()
    print('#SF-SORTER-RUNTIME#{:.3f}#'.format(timer))
    sorting = sorter.get_result()

    AutoSortingExtractor.write_sorting(sorting=sorting, save_path=sorting_out)

def _random_string(num_chars: int) -> str:
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(chars) for _ in range(num_chars))