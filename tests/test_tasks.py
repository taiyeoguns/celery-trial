from worker.tasks import sometask, slowtask
from unittest import mock


def test_sometask():
    assert sometask.run(2, 3) == 5


@mock.patch("worker.tasks.sleep")
@mock.patch("worker.tasks.requests.get")
def test_slowtask(mock_get, mock_sleep):
    response = mock.Mock()
    response.status_code = 201

    mock_get.return_value = response
    mock_sleep.return_value = 0

    assert slowtask.run() == 201
    mock_get.assert_called_once()
    mock_get.assert_called_once_with("https://misbehaving.site/delay/30")
    mock_sleep.assert_called_once_with(5)
