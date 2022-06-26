from collections import namedtuple

DataIngestionArtifact = namedtuple("DataIngestionArtifact", ["train_path",
                                                             "test_path","ingested_path"])   #Output file