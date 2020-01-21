from threeza.web import render_jsonpath, render_jsonpaths, render_mirror,render_pipe
import json


# --- Testing when they work ----
def test_render_mirror():
    instructions = "https://feeds.citibikenyc.com/stations/stations.json"
    res = render_mirror(instructions)
    assert "executionTime" in res.decode()
    res = render_mirror({"url":instructions})
    assert "executionTime" in res.decode()

def test_render_jsonpath():
    instructions = {"url":"https://feeds.citibikenyc.com/stations/stations.json",
                  "json_path":"$.stationBeanList[0]"}
    res = render_jsonpath(**instructions)
    assert "availableBikes" in res

def test_render_jsonpaths():
    instructions = {"url":"https://feeds.citibikenyc.com/stations/stations.json",
                  "json_paths":{"this_one":"$.stationBeanList[0]",
                                "that_one":"$.stationBeanList[1]"}
                   }
    res = render_jsonpaths(**instructions)
    assert "error" not in res
    assert "availableDocks" in json.loads(res)["this_one"]

def test_render_pipe():
    instructions = {"algo_name":"threezatests/double",
                   "input":3,
                   "api_key":"siml2eFEUW6jOI2w4Ivrq6LPr3L1"}
    res = render_pipe(**instructions)

# --- Testing when they dont ----



def test_render_mirror_fail():
    instructions = "https://feeds.citibikenyc.com/stations/stations__.json"
    res = render_mirror(instructions)
    assert "error" in res


def test_render_jsonpath_fail():
    instructions = {"url":"https://feeds.cit__ibikenyc.com/stations/stations.json",
                  "json_path":"$.stationBeanList[0]"}
    res = render_jsonpath(**instructions)
    assert "error" in res

def test_render_jsonpath_fail():
    instructions = {"url":"https://feeds.citibikenyc.com/stations/stations.json",
                  "json_path":"$.sta__tionBeanList[0]___.$.."}
    res = render_jsonpath(**instructions)
    assert "error" in res

def test_render_jsonpaths_fail():
    instructions = {"url":"https://feeds.citibikenyc.com/stations/stations.json",
                  "json_paths":{"this_one":"$.stationBeanList[0]",
                                "_$that_one":"$.stationB__eanList[1]"}
                   }
    res = render_jsonpaths(**instructions)
    assert "error" in res

def test_render_pipe_fail():
    instructions = {"algo_name":"threezatests/d__ouble",
                   "input":3,
                   "api_key":"siml2eFEUW6jOI2w4Ivrq6LPr3L1"}
    res = render_pipe(**instructions)
    assert "error" in res
