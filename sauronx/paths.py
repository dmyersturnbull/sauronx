import os

from klgists.common import pexists, pjoin

psize = os.path.getsize

sauronx_home = os.environ["SAURONX_HOME"]  # type: str

lock_file = pjoin(sauronx_home, ".lock")  # type: str


def processing_file(submission_hash: str) -> str:
    return pjoin(sauronx_home, ".processing-" + submission_hash)


def processing_submission_hash_from_file(submission_hash: str) -> str:
    return submission_hash[len(".processing-") :]


def component_check_path(output_dir: str, trigger: str) -> str:
    return pjoin(output_dir, trigger.lower())


def component_check_log_path(output_dir: str, trigger: str, filename: str) -> str:
    return pjoin(output_dir, trigger.lower(), filename)


class SubmissionPathCollection:
    def __init__(self, path: str, raw_frames_path: str, submission_hash: str):
        self.__path = path
        self.__raw_frames_path = raw_frames_path
        self.__submission_hash = submission_hash

    def output_dir(self):
        return self.__path

    def submission_hash(self) -> str:
        return self.__submission_hash

    def webcam_snapshot(self) -> str:
        return pjoin(self.__path, "sensors", "snap.jpg")

    def preview_snapshot(self) -> str:
        return pjoin(self.__path, "sensors", "preview.jpg")

    def microphone_wav_path(self) -> str:
        return pjoin(self.__path, "sensors", "microphone_log.wav")

    def microphone_flac_path(self) -> str:
        return pjoin(self.__path, "sensors", "microphone_log.flac")

    def microphone_timestamps_path(self) -> str:
        return pjoin(self.__path, "sensors", "microphone_times.txt")

    def avi_file(self) -> str:
        return pjoin(self.__path, "camera", "x265-crf15", "x265-crf15.mkv")

    def toml_file(self) -> str:
        return pjoin(self.__path, "config.toml")

    def env_file(self) -> str:
        return pjoin(self.__path, "environment.properties")

    def log_file(self) -> str:
        return pjoin(self.__path, "sauronx.log")

    def outer_frames_dir(self) -> str:
        return pjoin(self.__raw_frames_path)

    def trimmed_dir(self) -> str:
        return pjoin(self.__path, "trimmed_frames")

    def trimmed_start_video(self) -> str:
        return pjoin(self.__path, "trimmed_frames", "start.mkv")

    def trimmed_end_video(self) -> str:
        return pjoin(self.__path, "trimmed_frames", "end.mkv")

    def shasum_file(self) -> str:
        return pjoin(self.__path, "frames.7z.sha256")

    def stimulus_timing_log_file(self):
        return pjoin(self.__path, "timing", "stimuli.csv")

    def raw_snapshot_timing_log_file(self):
        return pjoin(self.__path, "timing", "raw_camera_timing.csv")

    def snapshot_timing_log_file(self):
        return pjoin(self.__path, "timing", "snapshots.list.csv")

    def start_events_log_file(self):
        return pjoin(self.__path, "timing", "start_events.csv")

    def end_events_log_file(self):
        return pjoin(self.__path, "timing", "end_events.csv")

    def avi_exists(self) -> bool:
        return (
            pexists(self.avi_file())
            and pexists(self.avi_file() + ".sha256")
            and psize(self.avi_file()) > 0
            and psize(self.avi_file() + ".sha256") > 0
        )

    def snapshot_timing_exists(self) -> bool:
        return (
            pexists(self.snapshot_timing_log_file())
            and psize(self.snapshot_timing_log_file()) > 0
            or pexists(self.raw_snapshot_timing_log_file())
            and psize(self.raw_snapshot_timing_log_file()) > 0
        )

    def stimulus_timing_exists(self) -> bool:
        return (
            pexists(self.stimulus_timing_log_file()) and psize(self.stimulus_timing_log_file()) > 0
        )
