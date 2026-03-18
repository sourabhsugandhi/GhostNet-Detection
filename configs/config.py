class Config:

    # -------------------
    # Dataset
    # -------------------
    NUM_CLASSES = 16
    IMAGE_SIZE = 640

    # -------------------
    # Training
    # -------------------
    BATCH_SIZE = 8
    EPOCHS = 100
    LR = 1e-3

    # Gradient accumulation
    ACCUMULATION_STEPS = 4

    # -------------------
    # Loss weights
    # -------------------
    CLS_LOSS_WEIGHT = 1.0
    BBOX_LOSS_WEIGHT = 3.0

    # -------------------
    # Weight clipping
    # -------------------
    WEIGHT_CLIP_VALUE = 0.1

    # -------------------
    # EMA
    # -------------------
    EMA_DECAY = 0.999

    # -------------------
    # Detection
    # -------------------
    CONF_THRESHOLD = 0.3
    NMS_IOU_THRESHOLD = 0.5

    # -------------------
    # FPN channels
    # -------------------
    FPN_OUT_CHANNELS = 256