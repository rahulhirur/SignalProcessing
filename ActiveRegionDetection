import numpy as np
from scipy.ndimage import label

def find_active_region(signal, threshold_factor=2.0):
    # Compute activity level of signal
    activity_level = np.sqrt(np.mean(np.square(signal)))
    
    # Set threshold
    threshold = threshold_factor * activity_level
    
    # Apply threshold to signal
    mask = np.zeros_like(signal)
    mask[signal >= threshold] = 1
    
    # Identify contiguous regions of mask
    labels, num_regions = label(mask)
    
    # Find largest contiguous region
    region_sizes = [np.sum(labels == i) for i in range(1, num_regions+1)]
    largest_region_label = np.argmax(region_sizes) + 1
    
    # Compute start and end indices of active region
    active_indices = np.where(labels == largest_region_label)[0]
    start_index, end_index = active_indices[0], active_indices[-1]
    
    return start_index, end_index
